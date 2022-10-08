<script>
	export let current_page;
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
</script>

<div>
    <button class:hidden={current_page < 3} on:click={() => dispatch('switch_page', current_page - 2)}>{current_page - 2}</button>
    <button class:hidden="{current_page < 2}" on:click={() => dispatch('switch_page', current_page - 1)}>{current_page - 1}</button>        
    <button>{current_page}</button>
    <!-- TODO: use next and previous fields of query for this -->
    <button on:click={() => dispatch('switch_page', current_page + 1)}>{current_page + 1}</button>
    <button on:click={() => dispatch('switch_page', current_page + 2)}>{current_page + 2}</button>
</div>


<style>
    .hidden {
        visibility: hidden;
    }
</style>