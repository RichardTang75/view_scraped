<script>
	import { onMount } from 'svelte';
    import Navigation from './navigation.svelte';
    import SourceColumn from './source_column.svelte';
    import AssignedColumn from './assigned_column.svelte';
	let item_list = [];
    let ignore_list = [];
    let want_list = [];
	let current_page = 1;
	onMount(async () => {
		item_list = await fetch_items(current_page);
		console.log(item_list)
	});
	async function switch_page(page) {
        // TODO: scroll to top
        // TODO: infinite scrolling?
		current_page = page;
        item_list = await fetch_items(current_page);
	}
    async function fetch_items(page) {
        // TODO: Need to filter in Django
        const item_response = await fetch('/api/items?page=' + page);
        const item_json = await item_response.json();
        return item_json.results;
    }
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
    function ignore(item) {
        if (ignore_list.includes(item.detail)) {
            // Should not happen. Throw error?
        }
        else {
            ignore_list = [...ignore_list, item.detail];
            item_list = item_list.filter(i => i !== item.detail);
        }
        // console.log(ignore_list);
        let ignore_item = {
            "item_id": item.detail.id,
            }
        console.log(ignore_item);
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
        // console.log(want_list);
        let want_item = {
            "item_id": item.detail.id,
            }
        console.log(want_item);
        post('/api/want/', want_item);
    }
</script>

<main>
    <div class="column_holder">
        <AssignedColumn item_list={ignore_list} />
        <SourceColumn {item_list} on:ignore={ignore} on:want={want} />
        <AssignedColumn item_list={want_list} />
    </div>
    <Navigation
        {current_page}
        {item_list}
        on:switch_page={(e) => switch_page(e.detail)}
    />
</main>

<style>
    main {
        text-align: center;
        padding: 1em;
        margin: 0 auto;
    }

    .item_div {
        /* text-align: left; */
        width: 80%;
        display: inline-block;
        /* border: 1px solid black; */
        background-color: #eee;
        margin: 0.5em;
        border-radius: 5px;
    }

    .item_div:hover {
        background-color: rgb(214, 224, 202);
    }

    .item_description {
        padding: 0 2em;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }

    .column_holder {
        display: flex;
        justify-content: space-between;
    }
</style>
