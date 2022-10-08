<script>
    export let item_list;
    export let is_want;
</script>

<div class='column'>
    <h1>{is_want ? 'Want' : 'Ignore'}</h1>
    <div class:want_background={is_want} class:ignore_background={!is_want}>
        {#each item_list as item}
            <div class="item_div">
                <h2>{item.title}</h2>
                <a href={item.link}>{item.link}</a>
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
        padding: 0 2em;
		background-color: #eee;
		border-radius: 5px;
    }
</style>