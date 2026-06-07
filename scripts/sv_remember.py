#!/usr/bin/env python3
"""sv-remember — file an agent-synthesized note into the SwarmVault inbox.

Reads the synthesized note body from stdin and writes a formatted markdown note
(frontmatter + body + Sources wikilinks) into the vault inbox for the next
nightly compile. Does NOT call SwarmVault — the calling agent is the synthesizer.
"""
import argparse
import datetime as dt
import re
import sys
from pathlib import Path

# Default to the inbox of whichever vault this script is deployed in
# (<vault>/scripts/sv_remember.py -> <vault>/inbox). Override with --inbox.
DEFAULT_INBOX = str(Path(__file__).resolve().parent.parent / "inbox")


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "note"


KIND_DIRS = {
    "source": "sources",
    "output": "outputs",
    "concept": "concepts",
    "entity": "entities",
    "module": "code",
}


def resolve_source(raw_id: str) -> str:
    raw_id = raw_id.strip()
    kind, sep, slug = raw_id.partition(":")
    if sep and slug:
        directory = KIND_DIRS.get(kind, "sources")
    else:
        directory, slug = "sources", raw_id
    return f"[[{directory}/{slug}]]"


def build_note(title: str, body: str, source_ids: list[str], tags: list[str], today: str) -> str:
    safe_title = title.replace('"', "'")
    all_tags = ["remembered", "synthesized-note", *tags]
    lines = [
        "---",
        f'title: "{safe_title}"',
        "source_type: synthesized-note",
        f"tags: [{', '.join(all_tags)}]",
        f"generated: {today}",
        "---",
        f"# {title}",
        "",
        body.strip(),
    ]
    links = [resolve_source(s) for s in source_ids if s.strip()]
    if links:
        lines += ["", "## Sources", *[f"- {link}" for link in links]]
    return "\n".join(lines) + "\n"


def split_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_args(argv):
    p = argparse.ArgumentParser(
        prog="sv-remember",
        description="File an agent-synthesized note into the SwarmVault inbox.",
    )
    p.add_argument("--title", required=True)
    p.add_argument("--sources", default="", help="comma-separated SwarmVault IDs")
    p.add_argument("--tags", default="", help="comma-separated extra tags")
    p.add_argument("--inbox", default=DEFAULT_INBOX)
    return p.parse_args(argv)


def main(argv=None, stdin=None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    stream = sys.stdin if stdin is None else stdin
    body = stream.read().strip()
    if not body:
        print("sv-remember: error: empty body on stdin", file=sys.stderr)
        return 1
    inbox = Path(args.inbox)
    if not inbox.is_dir():
        print(f"sv-remember: error: inbox not a directory: {inbox}", file=sys.stderr)
        return 1
    source_ids = split_csv(args.sources)
    tags = split_csv(args.tags)
    note = build_note(args.title, body, source_ids, tags, dt.date.today().isoformat())
    out = inbox / f"remembered-{slugify(args.title)}.md"
    out.write_text(note, encoding="utf-8")
    print(f"sv-remember: wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
