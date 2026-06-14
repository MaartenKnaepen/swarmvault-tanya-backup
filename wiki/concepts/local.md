---
page_id: 'concept:local'
kind: concept
cssclasses:
  - swarmvault
  - sv-concept
title: local
source_class: first_party
tags:
  - concept
source_ids:
  - swarmvault-config-a48adfce
project_ids: []
node_ids:
  - 'concept:local'
freshness: fresh
status: active
confidence: 0.65
created_at: '2026-05-22T19:04:20.085Z'
updated_at: '2026-06-13T23:55:23.815Z'
compiled_from:
  - swarmvault-config-a48adfce
managed_by: system
backlinks:
  - 'source:swarmvault-config-a48adfce'
schema_hash: 00d64cfa850a7f1b2281e664da3a51447f579da1e100ec5cb6e3b9247e3d47c2
source_hashes:
  swarmvault-config-a48adfce: a48adfced81a10f2038f523d6b935d4e392fd752cc7fc79d6c2306d5a13470b1
source_semantic_hashes:
  swarmvault-config-a48adfce: a48adfced81a10f2038f523d6b935d4e392fd752cc7fc79d6c2306d5a13470b1
decay_score: 1
last_confirmed_at: '2026-06-13T23:55:25.015Z'
---
# local

## Summary

Frequently referenced concept in swarmvault.config.

## Seen In

- [[sources/swarmvault-config-a48adfce|swarmvault.config]]

## Source Claims

- swarmvault.config Format: JSON Top-level: object Size: 13 Nested depth: 4 ## Schema - workspace: object (5 keys) - providers: object (1 keys) - tasks: object (5 keys) - viewer: object (1 keys) - profile: object (6 keys) - projects: object (0 keys) - agents: array (0 items) - schedules: object (0 keys) - orchestration: object (3 keys) - benchmark: object (3 keys) - repoAnalysis: object (2 keys) - graphSinks: object (0 keys) - retrieval: object (4 keys) ## Preview json { "workspace": { "rawDir": "raw", "wikiDir": "wiki", "stateDir": "state", "agentDir": "agent", "inboxDir": "inbox" }, "providers": { "local": { "type": "heuristic", "model": "heuristic-v1", "capabilities": [ "chat", "structured", "vision", "local" ] } }, "tasks": { "compileProvider": "local", "queryProvider": "local", "lintProvider": "local", "visionProvider": "local", "imageProvider": "local" }, "viewer": { "port": 4123 }, "profile": { "presets": [], "dashboardPack": "default", "guidedSessionMode": "insights_only", "dataviewBlocks": false, "guidedIngestDefault": false, "deepLintDefault": false }, "projects": {}, "agents": [], … [source:swarmvault-config-a48adfce]

