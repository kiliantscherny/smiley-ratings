<script>
	import '@evidence-dev/tailwind/fonts.css';
	import '../app.css';
	import { EvidenceDefaultLayout } from '@evidence-dev/core-components';
	import { base } from '$app/paths'; // Import base path
	export let data;
</script>

<EvidenceDefaultLayout
  {data}
  logo="{base}/smileys-logo.png"
  hideSidebar={false}
  hideBreadcrumbs={true}
  hideTOC={true}
  neverShowQueries={true}
>
  <slot slot="content" />
</EvidenceDefaultLayout>