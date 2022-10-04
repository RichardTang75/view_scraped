<script>
    export let item_list;
</script>

<div class='column'>
    <div>
        {#each item_list as item}
            <div class="item_div">
                <h2>{item.title}</h2>
                <a href={item.link}>{item.link}</a>
                <p class='item_description'>{item.description}</p>
            </div>
        {/each}
    </div>
</div>

<style>
    .column {
		/* border: 1px solid black; */
        background-color: rgb(250, 249, 214);
		margin: .5em;
		border-radius: 5px;
        flex-basis: 25%;
	}
</style>