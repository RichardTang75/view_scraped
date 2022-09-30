<script>
	import { onMount } from 'svelte';
    import Navigation from './navigation.svelte';
	let item_list = [
	];
	let current_page = 1;
	onMount(async () => {
		item_list = await fetch_items(current_page);
		console.log(item_list)
	});
	async function switch_page(page) {
		current_page = page;
        item_list = await fetch_items(current_page);
	}
    async function fetch_items(page) {
        const item_response = await fetch('/api/items?page=' + page);
        const item_json = await item_response.json();
        return item_json.results;
    }
</script>

<main>
	<div>
		{#each item_list as item}
			<div class="item_div">
				<h2>{item.title}</h2>
				<a href={item.link}>{item.link}</a>
				<p class='item_description'>{item.description}</p>
			</div>
		{/each}
	</div>
    <Navigation {current_page} {item_list} on:switch_page={(e)=>switch_page(e.detail)} />

</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	.item_div {
		/* text-align: left; */
		width: 80%;
		display: inline-block;
		/* border: 1px solid black; */
		background-color: #eee;
		margin: .5em;
		border-radius: 5px;
	}

	.item_div:hover {
		background-color: rgb(214, 224, 202);
	}

	.item_description {
		padding: 0 2em; 
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
	
</style>