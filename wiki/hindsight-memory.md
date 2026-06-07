---
shared-rules: true
lock: false
lock-updated: null
---
# Hindsight Memory Rules

## When to Retain
- End of every session (Hermes: automatic via auto_retain)
- Explicit preference, decision, or commitment stated in conversation
- Source material containing facts about Tanya or her projects

## How to Retain
- Always set context (specific: homeserver architecture discussion, not chat)
- Always set timestamp in ISO 8601
- Use stable document_id (session ID or semantic slug, never random UUID)
- Prefix with [hermes] or [claude] — required for audits
- Send raw conversation structure — never pre-summarise (destroys entity relationships)

## Recall vs Reflect
- Default: recall at budget mid before any context-dependent response
- Escalate to reflect only if recall results are fragmentary
- Never retain and recall in the same turn (retain is async)

## Do Not
- Embed tags inline in content — use the tags parameter
- Use random UUIDs as document_id (causes duplicates, blocks deduplication)
