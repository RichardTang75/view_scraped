<script>
    // TODO: prettify item divs
    // TODO: round corners of divs
    export let item_list;
</script>

<div class="column">
    <div>
        {#each item_list as item}
            <div class="item_div">
                <button class="assign_button">&lt;</button>
                <div class="item_description_div">
                    <h2>{item.title}</h2>
                    <a href={item.link}>{item.link}</a>
                    <p class="item_description">{item.description}</p>
                </div>
                <button class="assign_button">&gt;</button>
            </div>
        {/each}
    </div>
</div>

<style>
    .column {
        /* border: 1px solid black; */
        background-color: rgb(250, 249, 214);
        margin: 0.5em;
        border-radius: 5px;
        flex-basis: 50%;
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
    }
    .assign_button {
        padding: 1em; 
    }

	.item_div:hover {
		background-color: rgb(214, 224, 202);
	}
</style>
