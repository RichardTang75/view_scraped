<script>
	export let current_page;
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
</script>

<!-- TODO: solve unintuitive navigation bar -->
<div>
    {#if current_page > 2}
        <button on:click={() => dispatch('switch_page', current_page - 2)}>{current_page - 2}</button>
    {/if}
    {#if current_page > 1}
        <button on:click={() => dispatch('switch_page', current_page - 1)}>{current_page - 1}</button>
    {/if}
    <button on:click={() => dispatch('switch_page', current_page)}>{current_page}</button>
    <!-- TODO: use next and previous fields of query for this -->
    <button on:click={() => dispatch('switch_page', current_page + 1)}>{current_page + 1}</button>
    <button on:click={() => dispatch('switch_page', current_page + 2)}>{current_page + 2}</button>
</div>