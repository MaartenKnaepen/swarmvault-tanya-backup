---
page_id: 'graph:share-card'
kind: graph_report
cssclasses:
  - swarmvault
  - sv-graph-report
title: Share Card
tags:
  - graph
  - share
source_ids: &ref_1
  - candidates-5d9c2771
  - insights-1398dcf3
  - projects-acb5fd10
  - seerr-media-requests-available-ef141443
  - swarmvault-config-a48adfce
  - swarmvault-schema-b10ad2d9
project_ids: []
node_ids: &ref_0
  - 'concept:compile'
  - 'concept:index'
  - 'concept:object'
  - 'concept:keys'
  - 'concept:local'
  - 'source:insights-1398dcf3'
  - 'source:candidates-5d9c2771'
  - 'source:projects-acb5fd10'
freshness: fresh
status: active
confidence: 1
created_at: '2026-05-22T19:04:20.119Z'
updated_at: '2026-06-13T23:56:35.735Z'
compiled_from:
  - candidates-5d9c2771
  - insights-1398dcf3
  - projects-acb5fd10
  - seerr-media-requests-available-ef141443
  - swarmvault-config-a48adfce
  - swarmvault-schema-b10ad2d9
managed_by: system
backlinks: []
schema_hash: 00d64cfa850a7f1b2281e664da3a51447f579da1e100ec5cb6e3b9247e3d47c2
source_hashes: {}
source_semantic_hashes: {}
related_page_ids:
  - 'concept:compile'
  - 'concept:index'
  - 'concept:object'
  - 'concept:keys'
  - 'concept:local'
  - 'source:insights-1398dcf3'
  - 'source:candidates-5d9c2771'
  - 'source:projects-acb5fd10'
related_node_ids: *ref_0
related_source_ids: *ref_1
---
# SwarmVault Share Card

> A local-first map of knowledge-tanya: 6 sources compiled into 61 graph nodes and 71 wiki pages.

## Snapshot

- Sources: 6
- Wiki pages: 71
- Graph nodes: 61
- Graph edges: 62
- Communities: 5
- First-party focus: 48 nodes, 50 edges, 48 pages

## Highlights

- Top hubs: compile (21), index (14), object (12), keys (12), and local (12)
- Bridge nodes: Insights, Candidates, and Projects
- Surprising link: Candidates semantically_similar_to Insights. it crosses communities community:candidates-1 and community:insights-5; it spans different canonical pages; a bridge node is involved; This link is inferred from shared concepts...
- Surprising link: Insights semantically_similar_to Projects. it crosses communities community:insights-5 and community:candidates-1; it spans different canonical pages; a bridge node is involved; This link is inferred from shared concepts...
- Surprising link: swarmvault.config semantically_similar_to SwarmVault Schema. it crosses communities community:object-3 and community:should-4; it spans different canonical pages; a bridge node is involved; This link is inferred from shared tags.

## Ask Next

- Why does Insights connect multiple communities in the vault?
- Why does Candidates connect multiple communities in the vault?
- Why does Projects connect multiple communities in the vault?

## Share Post

```text
I scanned knowledge-tanya with SwarmVault: 6 sources -> 71 wiki pages, 61 graph nodes, 62 edges.
Top hubs: compile, index, and object.
Most surprising link: Candidates semantically_similar_to Insights.
Everything stays local. Try: npm install -g @swarmvaultai/cli && swarmvault quickstart ./your-repo
```

## Reproduce

```bash
npm install -g @swarmvaultai/cli
swarmvault quickstart ./your-repo
swarmvault graph share --post
```
