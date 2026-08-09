---
page_id: >-
  module:default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3
kind: module
cssclasses:
  - swarmvault
  - sv-module
title: Default to the inbox of whichever vault this script is deployed in module
source_class: first_party
tags:
  - module
  - code
  - python
source_ids:
  - default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3
project_ids: []
node_ids:
  - >-
    module:default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3
  - >-
    symbol:default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3:slugify.function
  - >-
    symbol:default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3:resolve-source.function
  - >-
    symbol:default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3:build-note.function
  - >-
    symbol:default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3:split-csv.function
  - >-
    symbol:default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3:parse-args.function
  - >-
    symbol:default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3:main.function
freshness: fresh
status: active
confidence: 1
created_at: '2026-06-30T20:23:20.549Z'
updated_at: '2026-08-09T00:08:29.244Z'
compiled_from:
  - default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3
managed_by: system
backlinks:
  - >-
    source:default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3
  - >-
    output:extract-all-text-from-the-following-pages-specifically-about-parents-helping-chi
  - >-
    output:what-are-the-gift-tax-schenkbelasting-rates-in-vlaanderen-for-parents-gifting-mo
  - >-
    output:what-are-the-legal-requirements-for-selling-a-rental-property-in-belgium-flander
schema_hash: 00d64cfa850a7f1b2281e664da3a51447f579da1e100ec5cb6e3b9247e3d47c2
source_hashes:
  default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3: f81e91f3e4a64f06e8847dc2b72fa5039c6167b690ee160502a4481720619774
source_semantic_hashes:
  default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3: f81e91f3e4a64f06e8847dc2b72fa5039c6167b690ee160502a4481720619774
related_page_ids:
  - >-
    source:default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3
  - >-
    output:extract-all-text-from-the-following-pages-specifically-about-parents-helping-chi
  - >-
    output:what-are-the-gift-tax-schenkbelasting-rates-in-vlaanderen-for-parents-gifting-mo
  - >-
    output:what-are-the-legal-requirements-for-selling-a-rental-property-in-belgium-flander
related_node_ids: []
related_source_ids:
  - default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3
  - schenkbelasting-da146a89
  - erfbelasting-b24e8569
  - seerr-media-requests-available-ef141443
  - zoeken-notaris-be-832736a2
  - swarmvault-schema-b10ad2d9
  - projects-acb5fd10
language: python
decay_score: 1
last_confirmed_at: '2026-08-09T00:08:31.631Z'
---
# Default to the inbox of whichever vault this script is deployed in module

Source ID: `default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3`
Source Path: `/mnt/data/knowledge-tanya/scripts/sv_remember.py`
Repo Path: `scripts/sv_remember.py`
Source Class: `first_party`
Language: `python`
Module Name: `scripts.sv_remember`
Source Page: [[sources/default-to-the-inbox-of-whichever-vault-this-script-is-deployed-in-f81e91f3|Default to the inbox of whichever vault this script is deployed in]]

## Summary

Default to the inbox of whichever vault this script is deployed in is a python module, defining 6 top-level symbol(s), exporting 6 symbol(s), depending on 5 external package import(s).

## Imports

- imports `argparse`
- imports `datetime` (namespace `dt`)
- imports `re`
- imports `sys`
- imports `pathlib` (named `Path`)

## Exports

- `slugify`
- `resolve_source`
- `build_note`
- `split_csv`
- `parse_args`
- `main`

## Symbols

- `slugify` (function, exported): def slugify(text: str) -> str: slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") return slug or "note"
- `resolve_source` (function, exported): def resolve_source(raw_id: str) -> str: raw_id = raw_id.strip() kind, sep, slug = raw_id.partition(":") if sep and slug: directory = KIND_DIRS.get(kind, "sources") else: directo...
- `build_note` (function, exported): def build_note(title: str, body: str, source_ids: list[str], tags: list[str], today: str) -> str: safe_title = title.replace('"', "'") all_tags = ["remembered", "synthesized-not...
- `split_csv` (function, exported): def split_csv(value: str) -> list[str]: return [item.strip() for item in value.split(",") if item.strip()]
- `parse_args` (function, exported): def parse_args(argv): p = argparse.ArgumentParser( prog="sv-remember", description="File an agent-synthesized note into the SwarmVault inbox.", ) p.add_argument("--title", requi...
- `main` (function, exported): def main(argv=None, stdin=None) -> int: args = parse_args(sys.argv[1:] if argv is None else argv) stream = sys.stdin if stdin is None else stdin body = stream.read().strip() if ...

## External Dependencies

- `argparse`
- `datetime`
- `re`
- `sys`
- `pathlib`

## Unresolved Local References

- No unresolved local references detected.

## Inheritance

- No inheritance relationships detected.

## Calls

- `build_note` calls `resolve_source`
- `main` calls `slugify`
- `main` calls `build_note`
- `main` calls `split_csv`
- `main` calls `parse_args`
- `main` calls `Path`

## Diagnostics

- No parser diagnostics.

## Related Outputs

- [[outputs/extract-all-text-from-the-following-pages-specifically-about-parents-helping-chi|Extract all text from the following pages specifically about parents helping children buy a house: 1) The Vlaanderen.be schenkbelasting (gift tax) page - what are the rates, exemptions, conditions for gifting money or property to children for a home purchase? 2) The notaris.be search results for "borgstelling" (suretyship/guarantee) - what does it say about parents acting as guarantor for children's mortgage? 3) The NBB Centrale voor Kredieten aan Particulieren page - what does it say about how this credit registry works, especially related to mortgages and guarantors?]]
- [[outputs/what-are-the-gift-tax-schenkbelasting-rates-in-vlaanderen-for-parents-gifting-mo|What are the gift tax (schenkbelasting) rates in Vlaanderen for parents gifting money to children for a house purchase? Include the tax rates for different amounts, the annual exemption amounts, and any specific conditions or recent changes (2024-2026).]]
- [[outputs/what-are-the-legal-requirements-for-selling-a-rental-property-in-belgium-flander|What are the legal requirements for selling a rental property in Belgium Flanders 2025-2026?]]

