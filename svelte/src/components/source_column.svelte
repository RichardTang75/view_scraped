<script>
    // TODO: prettify item divs
    // TODO: round corners of divs
    // TODO: deal with height of page changing
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    export let item_list;
    let selected_item = null;
    let show_iframe = false;
    let iframe_div;
    console.log(show_iframe)

    function set_iframe(item) {
        if ((selected_item === item) && (show_iframe === true)) {
            show_iframe = false;
        }
        else {
            show_iframe = true;
        }
        selected_item = item;
    }
    function close_iframe() {
        show_iframe = false;
    }
</script>

<div class="column source_column">
    <h1>View Scraped</h1>
    <div class="source_background">
        {#each item_list as item}
            <div class="item_div">
                <button on:click="{() => dispatch('ignore', item)}" class="assign_button">&lt;</button>
                <div class=item_with_info_div>
                    <div class="item_description_div">
                        <h2>{item.title}</h2>
                        <a href={item.link}>{item.link}</a>
                        <p class="item_description">{item.description}</p>
                    </div>
                    <button class="info_button" on:click="{() => set_iframe(item)}">View</button>
                </div>
                <button on:click="{() => dispatch('want', item)}" class="assign_button">&gt;</button>
            </div>
        {/each}
    </div>
    <div class='spacer' class:hidden={!show_iframe}></div>
</div>


<!-- TODO: put this in its own component -->
<!-- TODO: redesign with this in mind -->
{#if selected_item}
    <div bind:this={iframe_div} class:hidden={!show_iframe} class="info_iframe">
        <button class:hidden={!show_iframe} class='info_button' on:click="{() => close_iframe()}">X</button>
        <iframe src={selected_item.link} class="iframe"></iframe>
    </div>
{/if}


<style>
    .hidden {
        display: none;
    }
    .source_column {
        flex-basis: 50%;
    }
    .spacer {
        height: 50vh;
        flex-shrink: 0;
    }
    .source_background {
        background-color: rgb(250, 249, 214);
        height: 100%;
    }
    .item_with_info_div {
        width: 100%;
    }
    .assign_button {
        padding: 1em; 
    }
    .info_button {
        padding: .5em;
        width: 100%;
    }

	.item_div:hover {
		background-color: rgb(214, 224, 202);
    }

        /* floating div taking up bottom half of screen */
    .info_iframe {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 50%;
        border: none;
        background-color: #eee;
    }

    .iframe {
        width: 100%;
        height: 100%;
    }
</style>
