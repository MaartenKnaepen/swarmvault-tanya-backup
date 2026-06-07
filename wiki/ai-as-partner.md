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
- When unsure → do both, or ask Tanya

## Persisting Write-ups
A structured write-up/analysis is persisted by writing a markdown note into the vault **inbox** (`<vault>/inbox/`); the nightly compile folds it into the wiki + graph. Never use `query_vault` with `save: true` — it runs a per-query mini-compile and stalls. Query with `save: false`.
- On Trident: pipe the note body to `<vault>/scripts/sv-remember --title "..." --sources <ids> --tags <tags>` — it formats frontmatter + `[[wikilinks]]` and self-locates to its own vault's inbox.
- Cross-network: drop the `.md` into the Syncthing-synced inbox folder; it replicates to Trident.
- Capture = inbox write (batched into the nightly compile). Querying = MCP (`query_vault`/`search_pages`), which works over HTTP across networks.

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
| Conflict resolution | Always Tanya |

## Proposals
Append-only at bottom of this page.
Format: [YYYY-MM-DDThh:mm] [agent/tanya]: <text>
When resolved: move full thread to log.md, update page with final decision.

## Hard Limits
- 500-line budget per shared-rules page. Rationale lives in log.md, not here.
- Each agent keeps a local mirror of these rules for when the wiki is unreachable.
