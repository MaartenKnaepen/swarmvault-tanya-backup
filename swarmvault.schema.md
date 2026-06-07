# SwarmVault Schema

## Vault Purpose

General-purpose personal knowledge base for Tanya. Contains durable reference
material, research, notes, media transcripts, code, and structured knowledge.
Ephemeral facts and preferences belong in Hindsight (see wiki/ai-as-partner.md).

## Naming Conventions

- Page titles: lowercase-kebab-case, descriptive, stable
- Sources: preserve original titles where meaningful
- Concepts: noun phrases (e.g., distributed-systems, rust-ownership)
- Entities: proper names (e.g., karpathy, anthropic)

## Page Structure Rules

- Source pages stay grounded in original material
- Concept pages aggregate claims from multiple sources
- Entity pages collect facts about people, orgs, tools, projects
- Preserve contradictions; note them explicitly

## Categories

### Sources (by content type, not topic)

- reference: books, papers, documentation
- article: blog posts, news, essays
- note: personal writing, meeting notes, ideas
- transcript: audio, video, conversation exports
- data: spreadsheets, datasets, exports

### Wiki

- concept: ideas, patterns, techniques
- entity: people, organizations, tools, projects
- project: active work with context

## Relationship Types

- cites, supports, contradicts, extends
- authored-by, affiliated-with, depends-on
- tagged (soft categorization)

## Grounding Rules

- All foreign-language content must be transcribed/translated to English before
  ingestion. Originals retained in raw/ but wiki synthesis uses English only.
- Prefer raw sources over summaries
- Cite source IDs for all claims
- Never treat wiki as source of truth when raw material disagrees
- User facts → Hindsight, not wiki pages (see wiki/ai-as-partner.md)

## Exclusions

- No pages for ephemeral scheduling, todos, or calendar items
- No pages for personal preferences or decisions (→ Hindsight)
- No sensitive credentials, API keys, or passwords
- No auto-generated boilerplate without substantive content
