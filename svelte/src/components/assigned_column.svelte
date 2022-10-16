<script>
    export let item_list;
    export let is_want;
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
</script>

<div class='column'>
    <h1>{is_want ? 'Want' : 'Ignore'}</h1>
    <div class:want_background={is_want} class:ignore_background={!is_want}>
        {#each item_list.slice(-5) as item}
            <div class="item_div">
                {#if is_want}
                    <button on:click="{() => dispatch('delete_want', item)}" class="assign_button">&lt;</button>
                {/if}
                <div class="item_description_div">
                    <h2>{item.title}</h2>
                    <a href={item.link}>{item.link}</a>
                </div>
                {#if !is_want}
                    <button on:click="{() => dispatch('delete_ignore', item)}" class="assign_button">&gt;</button>
                {/if}
                <!-- <p class='item_description'>{item.description}</p> -->
            </div>
        {/each}
    </div>
</div>

<style>
    .column {
        margin: 0.5em;
        border-radius: 5px;
        flex-basis: 25%;
        flex-direction: column;
        display: flex;
    }
    .ignore_background {
        background-color: rgb(255, 225, 200);
        height: 100%;
    }
    .want_background {
        background-color: rgb(207, 215, 248);
        height: 100%;
    }
    .item_div {
        display: flex;
        justify-content: space-between;
        align-items: stretch;
        /* width: 80%; */
		background-color: #eee;
		border-radius: 5px;
    }
    .item_description_div {
        padding: 0 2em;
        word-break: break-word;
    }
    .assign_button {
        padding: 1em; 
    }
</style>