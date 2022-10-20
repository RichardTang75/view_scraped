<script>
	export let current_page;
    export let item_count;
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
</script>

<div>
    <button class:invisible={current_page < 3} on:click={() => dispatch('switch_page', current_page - 2)}>{current_page - 2}</button>
    <button class:invisible="{current_page < 2}" on:click={() => dispatch('switch_page', current_page - 1)}>{current_page - 1}</button>        
    <button>{current_page}</button>
    <!-- TODO: use next and previous fields of query for this -->
    <button class:invisible="{current_page >= item_count / 10}" on:click={() => dispatch('switch_page', current_page + 1)}>{current_page + 1}</button>
    <button class:invisible="{current_page >= item_count / 10 - 1}" on:click={() => dispatch('switch_page', current_page + 2)}>{current_page + 2}</button>
</div>


<style>
    .invisible {
        visibility: hidden;
    }
</style>