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
    function want(item) {
        if (want_list.includes(item.detail)) {
            // Should not happen.
        }
        else {
            want_list = [...want_list, item.detail];
            item_list = item_list.filter(i => i !== item.detail);
        }
        let want_item = {
            "item_id": item.detail.id,
            }
        post('/api/want/', want_item);
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
                    <div class="item_div" on:click={() => set_iframe(item)}>
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
                        <button class='info_button' on:click="{() => close_iframe()}">Completed</button>
                        <button class='info_button' on:click="{() => close_iframe()}">Queue</button>
                        <button class='info_button' on:click="{() => close_iframe()}">Reject</button>
                        <button class='info_button' on:click="{() => close_iframe()}">X</button>
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
</style>
