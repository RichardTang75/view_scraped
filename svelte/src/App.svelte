<script>
	import { Router } from "@roxi/routify";
	import { routes } from "../.routify/routes";
</script>
<Router {routes} />

<style>
    :global(main) {
        text-align: center;
        padding: 1em;
        margin: 0 auto;
    }

    :global(.column_holder) {
        display: flex;
        justify-content: space-between;
    }

    :global(h2) {
        margin: 0;
        padding: .5em;
    }

    :global(.column) {
        margin: 0.5em;
        border-radius: 5px;
        display: flex;
        flex-direction: column;
    }

    :global(.item_div) {
        display: flex;
        justify-content: space-between;
        align-items: stretch;
        /* width: 80%; */
		background-color: #eee;
		border-radius: 5px;
    }

	:global(.item_div:hover) {
		background-color: rgb(214, 224, 202);
    }
	:global(.item_description_div) {
        padding: 0 2em;
        word-break: break-word;
    }
</style>
