<script>
	import { onMount } from 'svelte';
    import Navigation from '../components/navigation.svelte';
    import SourceColumn from '../components/source_column.svelte';
	let item_list = [];
	let current_page = 1;
    let item_count = 0;
	onMount(async () => {
		item_list = await fetch_items(current_page);
	});
	async function switch_page(page) {
		current_page = page;
        item_list = await fetch_items(current_page);
	}
    async function fetch_items(page) {
        const item_response = await fetch('/api/act_want/?page=' + page);
        const item_json = await item_response.json();
        item_count = item_json.count;
        console.log(item_json.results);
        // console.log(item_json.results.slice(-11));
        selected_item = item_json.results[0];
        show_iframe = true;
        return item_json.results;
    }
    // TODO: Combine posts/deletes?
    async function post(url, item) {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(item)
        });
        console.log(JSON.stringify(item));
        const json = await response.json();
        console.log(json);
    }
    async function delete_item(url) {
        const response = await fetch(url, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
        });
        console.log(response.status);
    }
    async function update_item(url, item) {
        const response = await fetch(url, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(item)
        });
        console.log(JSON.stringify(item));
        const json = await response.json();
        console.log(json);
    }
    // update item to complete
    function complete_want(item) {
        item.completed = true;
        let want_item_id = item.item_id.id
        item.item_id = want_item_id
        update_item('/api/want/' + want_item_id + '/', item);
        item_list = item_list.filter(i => i !== item);
        selected_item = null;
        show_iframe = false;
    }
    // queue item by changing view order
    function queue_want(item) {
        item.view_order += 1;
        let want_item_id = item.item_id.id
        item.item_id = want_item_id
        update_item('/api/want/' + want_item_id + '/', item);
        item_list = item_list.filter(i => i !== item);
        selected_item = null;
        show_iframe = false;
    }
    // delete item
    function delete_want(item) {
        let want_item_id = item.item_id.id
        delete_item('/api/want/' + want_item_id + '/');
        item_list = item_list.filter(i => i !== item);
        selected_item = null;
        show_iframe = false;
    }

    let selected_item = null;
    let show_iframe = false;

    function set_iframe(item) {
        if ((selected_item === item) && (show_iframe === true)) {
            show_iframe = false;
        }
        else {
            show_iframe = true;
        }
        selected_item = item;
    }
    function close_iframe() {
        show_iframe = false;
    }
</script>

<main>
    <div class="column_holder">
        <div class="column source_column">
            <h1>View Scraped</h1>
            <div class="source_background">
                {#each item_list as item}
                <!-- on click pass the item_div -->
                    <div class="item_div" class:active_select={selected_item === item} on:click={() => set_iframe(item)}>
                        <div class="item_description_div">
                            <h2>{item.item_id.title}</h2>
                            <a href={item.item_id.link}>{item.item_id.link}</a>
                            <p class="item_description">{item.item_id.description}</p>
                        </div>
                    </div>
                {/each}
            </div>
        </div>
        <div class="column iframe_column">
            {#if selected_item}
                <div class:hidden={!show_iframe} class="info_iframe">
                    <div class="iframe_button_div">
                        <button class='info_button complete_button' on:click="{() => complete_want(selected_item)}">Complete</button>
                        <button class='info_button queue_button' on:click="{() => queue_want(selected_item)}">Queue</button>
                        <button class='info_button reject_button' on:click="{() => delete_want(selected_item)}">Reject</button>
                        <button class="info_button close_button" on:click="{() => close_iframe()}">X</button>
                    </div>
                    <iframe src={selected_item.item_id.link} class="iframe"></iframe>
                </div>
            {/if}
        </div>
    </div>
    <Navigation
        {current_page}
        {item_count}
        on:switch_page={(e) => switch_page(e.detail)}
    />
</main>

<style>
    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
    .hidden {
        display: none;
    }
    .source_column {
        flex-basis: 40%;
    }
    .iframe_column {
        flex-basis: 60%;
        height: 100vh;
    }
    .info_iframe {
        width: 100%;
        height: 100%;
        border: none;
        background-color: #eee;
    }
    .iframe_button_div {
        display: flex;
        flex-direction: row;
        justify-content: flex-end;
        padding: 0.5rem;
    }

    .iframe {
        width: 100%;
        height: 100%;
    }
    .info_button {
        margin: 0.5rem;
        padding: 0.5rem;
        border-radius: 0.5rem;
        /* background-color: #eee; */
        flex-basis: 10rem;
    }
    .complete_button {
        background-color: rgb(217, 255, 217);
    }
    .queue_button {
        background-color: rgb(255, 255, 217);
    }
    .reject_button {
        background-color: rgb(255, 217, 217);
    }
    .close_button {
        background-color: rgb(255, 119, 119);
    }
    .active_select{
        border: 1px solid #000;
        background-color: #eee;
    }
</style>
