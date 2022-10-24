<script>
	import { onMount } from 'svelte';
    import Navigation from './navigation.svelte';
    import SourceColumn from './source_column.svelte';
    import AssignedColumn from './assigned_column.svelte';
	let item_list = [];
    let ignore_list = [];
    let want_list = [];
	let current_page = 1;
    let item_count = 0;
	onMount(async () => {
		item_list = await fetch_items(current_page);
	});
	async function switch_page(page) {
        // TODO: scroll to top
        // TODO: infinite scrolling?
		current_page = page;
        item_list = await fetch_items(current_page);
	}
    async function fetch_items(page) {
        const item_response = await fetch('/api/items/?page=' + page);
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
    // TODO: Combine all ignore/wants
    function ignore(item) {
        if (ignore_list.includes(item.detail)) {
            // Should not happen. Throw error?
        }
        else {
            ignore_list = [...ignore_list, item.detail];
            item_list = item_list.filter(i => i !== item.detail);
        }
        let ignore_item = {
            "item_id": item.detail.id,
            }
        post('/api/ignore/', ignore_item);
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
    function delete_ignore(item) {
        if (ignore_list.includes(item.detail)) {
            ignore_list = ignore_list.filter(i => i !== item.detail);
            // TODO: add to item_list. fetch it again?
        }
        else {
            // Should not happen.
        }
        let delete_url = '/api/ignore/' + item.detail.id + '/';
        delete_item(delete_url);
    }
    function delete_want(item) {
        if (want_list.includes(item.detail)) {
            want_list = want_list.filter(i => i !== item.detail);
        }
        else {
            // Should not happen.
        }
        let delete_url = '/api/want/' + item.detail.id + '/';
        delete_item(delete_url);
    }
    // $: {
    //     let items_left = item_list.length;
    //     if (items_left < 5 && current_page < item_count / 10) {
    //         fetch_items(current_page + 1).then(
    //             new_items => {
    //                 item_list = [...item_list, ...new_items];
    //             }
    //         );
    //     }
    // }
</script>

<main>
    <div class="column_holder">
        <AssignedColumn item_list={ignore_list} is_want={false} on:delete_ignore={delete_ignore}/>
        <SourceColumn {item_list} on:ignore={ignore} on:want={want} />
        <AssignedColumn item_list={want_list} is_want={true} on:delete_want={delete_want}/>
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
</style>
