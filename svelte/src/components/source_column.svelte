<script>
    // TODO: prettify item divs
    // TODO: round corners of divs
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    export let item_list;
</script>

<div class="column">
    <h1>View Scraped</h1>
    <div class="source_background">
        {#each item_list as item}
            <div class="item_div">
                <button on:click="{() => dispatch('ignore', item)}" class="assign_button">&lt;</button>
                <div class="item_description_div">
                    <h2>{item.title}</h2>
                    <a href={item.link}>{item.link}</a>
                    <p class="item_description">{item.description}</p>
                </div>
                <button on:click="{() => dispatch('want', item)}" class="assign_button">&gt;</button>
            </div>
        {/each}
    </div>
</div>

<style>
    .column {
        margin: 0.5em;
        border-radius: 5px;
        flex-basis: 50%;
        display: flex;
        flex-direction: column;
    }
    .source_background {
        background-color: rgb(250, 249, 214);
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

	.item_div:hover {
		background-color: rgb(214, 224, 202);
	}
</style>
