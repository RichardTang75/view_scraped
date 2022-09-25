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
			<div class="item_description">
				<h2>{item.title}</h2>
				<a href={item.link}>{item.link}</a>
				<p>{item.description}</p>
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

	.item_description {
		/* text-align: left; */
		width: 80%;
		display: inline-block;
		border: 1px solid black;
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