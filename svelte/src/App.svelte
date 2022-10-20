<!-- <script>
	import ViewScraped from "./components/ViewScraped.svelte";
</script>

<ViewScraped /> -->

<script>
	import { Router } from "@roxi/routify";
	import { routes } from "../.routify/routes";
</script>
<Router {routes} />