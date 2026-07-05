# swarmvault.config
Format: JSON
Top-level: object
Size: 13
Nested depth: 4

## Schema

- workspace: object (5 keys)
- providers: object (2 keys)
- tasks: object (6 keys)
- viewer: object (1 keys)
- profile: object (6 keys)
- projects: object (0 keys)
- agents: array (0 items)
- schedules: object (0 keys)
- orchestration: object (3 keys)
- benchmark: object (3 keys)
- repoAnalysis: object (2 keys)
- graphSinks: object (0 keys)
- retrieval: object (4 keys)

## Preview

```json
{
  "workspace": {
    "rawDir": "raw",
    "wikiDir": "wiki",
    "stateDir": "state",
    "agentDir": "agent",
    "inboxDir": "inbox"
  },
  "providers": {
    "local": {
      "type": "heuristic",
      "model": "heuristic-v1",
      "capabilities": [
        "chat",
        "structured",
        "vision",
        "local"
      ]
    },
    "ollama-embed": {
      "type": "openai",
      "baseUrl": "http://localhost:11434/v1",
      "apiKey": "ollama",
      "model": "hf.co/jinaai/jina-embeddings-v5-text-small-retrieval-GGUF:Q4_K_M",
      "capabilities": ["embeddings"]
    }
  },
  "tasks": {
    "compileProvider": "local",
    "queryProvider": "local",
    "lintProvider": "local",
    "visionProvider": "local",
    "imageProvider": "local",
    "embeddingProvider": "ollama-embed"
  },
  "viewer": {
    "port": 4124
  },
  "profile": {
    "presets": [],
…
```