<script>
	import { onMount } from 'svelte';
	let item_list = [
	];
	let current_page = 1;
	onMount(async () => {
		const item_response = await fetch('/api/items');
		const item_json = await item_response.json();
		item_list = item_json.results;
		console.log(item_list)
	});
	async function switch_page(page) {
		current_page = page;
		const item_response = await fetch('/api/items?page=' + page);
		const item_json = await item_response.json();
		item_list = item_json.results;
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
	<div>
		{#if current_page > 2}
			<button on:click={() => switch_page(current_page - 2)}>{current_page - 2}</button>
		{/if}
		{#if current_page > 1}
			<button on:click={() => switch_page(current_page - 1)}>{current_page - 1}</button>
		{/if}
		<button on:click={() => switch_page(current_page)}>{current_page}</button>
		<button on:click={() => switch_page(current_page + 1)} disabled={item_list.length < 10}>{current_page + 1}</button>
		<button on:click={() => switch_page(current_page + 2)} disabled={item_list.length < 10}>{current_page + 2}</button>
	</div>

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