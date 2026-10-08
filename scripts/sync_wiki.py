#!/usr/bin/env python3
"""Copy the Obsidian wiki into Quartz's content/ folder, sanitized for public release.

Usage: python3 scripts/sync_wiki.py <path-to-vault>/Atlas/Wiki

What it does:
  * wipes content/ and copies every .md page from the wiki, except EXCLUDE
  * drops the `pdf:` frontmatter field (it points at local PDF copies)
  * turns wiki-links into vault files outside the wiki (PDFs, course folders)
    into plain text, so no local file paths become links
  * turns wiki-links to excluded pages into plain text
"""
import re
import shutil
import sys
from pathlib import Path

# Pages that are never published (basename without .md).
EXCLUDE = {
    "agent-prompt",  # internal LLM-maintenance prompt
    "dashboard",  # Dataview queries; don't render on the web
}

# Unpublished third-party work: held back until the author confirms it can be public.
HOLD = {
    "Varney 2026 PatchesChapter",
}

SKIP = EXCLUDE | HOLD
LINK = re.compile(r"(!?)\[\[([^\]|#]+)(#[^\]|]*)?(\|[^\]]*)?\]\]")


def fix_links(text: str) -> str:
    def repl(m: re.Match) -> str:
        bang, target, heading, alias = m.groups()
        name = target.strip()
        external = "/" in name and not name.startswith(("Concepts/", "Entities/", "People/", "Sources/", "Derivations/"))
        base = Path(name).name.removesuffix(".pdf").removesuffix(".md")
        if external or base in SKIP:
            if alias:
                return alias[1:]
            return base if external else name
        return m.group(0)

    return LINK.sub(repl, text)


def split_display_math(text: str) -> str:
    """Put multi-line $$ fences on their own lines.

    Obsidian accepts `$$\\begin{aligned}` ... `\\end{aligned}$$`, but remark-math treats text after an
    opening `$$` as a fence label and drops it, which breaks the environment.
    """
    out, in_block = [], False
    for line in text.split("\n"):
        s = line.strip()
        if not in_block and s.startswith("$$") and s != "$$" and "$$" not in s[2:]:
            out += ["$$", s[2:]]
            in_block = True
        elif not in_block and s == "$$":
            out.append(line)
            in_block = True
        elif in_block and s.endswith("$$"):
            if s != "$$":
                out.append(s[:-2])
            out.append("$$")
            in_block = False
        else:
            out.append(line)
    return "\n".join(out)


def strip_pdf_field(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---", 4)
    if end < 0:
        return text
    front = "\n".join(l for l in text[4:end].split("\n") if not l.startswith("pdf:"))
    return "---\n" + front + text[end:]


def main() -> None:
    src = Path(sys.argv[1]).resolve()
    dst = Path(__file__).resolve().parent.parent / "content"
    if not (src / "index.md").exists():
        sys.exit(f"{src} does not look like the wiki (no index.md)")
    shutil.rmtree(dst, ignore_errors=True)
    n = 0
    for page in sorted(src.rglob("*.md")):
        if page.stem in SKIP:
            continue
        out = dst / page.relative_to(src)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(split_display_math(fix_links(strip_pdf_field(page.read_text()))))
        n += 1
    print(f"copied {n} pages to {dst} (excluded: {', '.join(sorted(SKIP))})")


if __name__ == "__main__":
    main()
