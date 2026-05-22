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
  - swarmvault-config-a48adfce
  - swarmvault-schema-b10ad2d9
project_ids: []
node_ids: &ref_0
  - 'concept:compile'
  - 'concept:index'
  - 'concept:object'
  - 'concept:keys'
  - 'concept:local'
  - 'source:candidates-5d9c2771'
  - 'source:insights-1398dcf3'
freshness: fresh
status: active
confidence: 1
created_at: '2026-05-22T19:04:20.119Z'
updated_at: '2026-05-22T19:04:20.396Z'
compiled_from:
  - candidates-5d9c2771
  - insights-1398dcf3
  - projects-acb5fd10
  - swarmvault-config-a48adfce
  - swarmvault-schema-b10ad2d9
managed_by: system
backlinks: []
schema_hash: 874431dbbfdec0b254a4aa1bf002900574c9b485735a883690c2becb5f717720
source_hashes: {}
source_semantic_hashes: {}
related_page_ids:
  - 'concept:compile'
  - 'concept:index'
  - 'concept:object'
  - 'concept:keys'
  - 'concept:local'
  - 'source:candidates-5d9c2771'
  - 'source:insights-1398dcf3'
related_node_ids: *ref_0
related_source_ids: *ref_1
---
# SwarmVault Share Card

> A local-first map of knowledge-tanya: 5 sources compiled into 48 graph nodes and 57 wiki pages.

## Snapshot

- Sources: 5
- Wiki pages: 57
- Graph nodes: 48
- Graph edges: 49
- Communities: 5
- First-party focus: 48 nodes, 49 edges, 48 pages

## Highlights

- Top hubs: compile (21), index (14), object (12), keys (12), and local (12)
- Bridge nodes: Candidates, Insights, and compile
- Surprising link: Candidates semantically_similar_to Projects. it crosses communities community:candidates-4 and community:compile-3; it spans different canonical pages; a bridge node is involved; This link is inferred from shared concepts....
- Surprising link: Candidates semantically_similar_to Insights. it crosses communities community:candidates-4 and community:insights-5; it spans different canonical pages; a bridge node is involved; This link is inferred from shared concepts...
- Surprising link: Insights semantically_similar_to Projects. it crosses communities community:insights-5 and community:compile-3; it spans different canonical pages; a bridge node is involved; This link is inferred from shared concepts.; ...

## Ask Next

- Why does Candidates connect multiple communities in the vault?
- Why does Insights connect multiple communities in the vault?
- Why does compile connect multiple communities in the vault?

## Share Post

```text
I scanned knowledge-tanya with SwarmVault: 5 sources -> 57 wiki pages, 48 graph nodes, 49 edges.
Top hubs: compile, index, and object.
Most surprising link: Candidates semantically_similar_to Projects.
Everything stays local. Try: npm install -g @swarmvaultai/cli && swarmvault quickstart ./your-repo
```

## Reproduce

```bash
npm install -g @swarmvaultai/cli
swarmvault quickstart ./your-repo
swarmvault graph share --post
```
