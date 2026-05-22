---
shared-rules: true
lock: false
lock-updated: null
---
# AI-as-Partner Protocol

## Routing Rules
- Conversation facts, preferences, decisions → Hindsight retain
- Documents, sources, URLs, audio/video → SwarmVault ingest
- Structured write-ups and analyses → SwarmVault wiki page
- When unsure → do both, or ask Maarten

## Concurrent Edit Protocol (Soft-Lock)
Before editing any shared-rules page:
1. Check that lock: false
2. Set lock: true and lock-updated: <ISO timestamp>
3. Make edits
4. Set lock: false in the same write

A lock older than 30 minutes is stale and may be overridden with a log entry.

## Division of Labour
| Domain | Owner |
|---|---|
| Automation, cron, scripts | Hermes |
| Complex coding, reasoning, drafting | Claude Code |
| Wiki page authoring (substantive) | Either |
| Shared rules pages | Negotiated via Proposals |
| Hindsight memory writes | Both (prefix [hermes] or [claude]) |
| Weekly vault maintenance | Hermes (Sunday cron) |
| Conflict resolution | Always Maarten |

## Proposals
Append-only at bottom of this page.
Format: [YYYY-MM-DDThh:mm] [agent/maarten]: <text>
When resolved: move full thread to log.md, update page with final decision.
