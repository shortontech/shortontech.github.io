#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


ROOT = Path(__file__).resolve().parent
LIBRARY = ROOT / "library" / "whitepapers"
TEMPLATES = ROOT / "templates"
PUBLIC_WHITEPAPERS = ROOT / "whitepapers"
DIST_WHITEPAPERS = ROOT / "dist" / "whitepapers"

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SECTION_RE = re.compile(r"^(\d{2})-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")

TAG_LABELS = {
    "proof-driven-appsec": "Proof-Driven AppSec",
    "sast": "SAST",
    "dast": "DAST",
    "evidence": "Evidence",
    "ai-security": "AI Security",
    "secure-codegen": "Secure Codegen",
    "authorization": "Authorization",
    "taint": "Taint",
    "browser-evidence": "Browser Evidence",
    "agents": "Agents",
    "ai-labor": "AI Labor",
    "industrial-capacity": "Industrial Capacity",
    "research-ops": "Research Ops",
    "workforce-development": "Workforce Development",
}

FEATURED_TAGS = [
    "proof-driven-appsec",
    "ai-security",
    "secure-codegen",
]


@dataclass
class Paper:
    title: str
    slug: str
    published_at: datetime
    published_at_raw: str
    display_date: str
    status: str
    tags: list[str]
    tag_items: list[dict[str, str]]
    summary: str
    source_path: Path
    section_paths: list[Path]
    content_markdown: str
    content_html: str


def fail(message: str) -> None:
    print(f"generate.py: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        fail(f"{path} must contain a YAML object")
    return data


def require_string(data: dict, key: str, path: Path) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(f"{path} must define non-empty string field `{key}`")
    return value.strip()


def parse_published_at(data: dict, path: Path) -> tuple[datetime, str, str]:
    raw_value = data.get("published_at")
    if raw_value is None:
        fail(f"{path} must define `published_at`, for example 2026-06-08T00:00:00-07:00")

    if isinstance(raw_value, datetime):
        dt = raw_value
        raw = dt.isoformat()
    elif isinstance(raw_value, str):
        raw = raw_value.strip()
        if raw.endswith("Z"):
            raw = raw[:-1] + "+00:00"
        try:
            dt = datetime.fromisoformat(raw)
        except ValueError:
            fail(f"{path} has invalid `published_at`: {raw_value!r}")
    else:
        fail(f"{path} `published_at` must be an ISO 8601 datetime string")

    return dt, raw, dt.strftime("%B %-d, %Y")


def load_sections(path: Path) -> tuple[list[Path], str]:
    section_paths = sorted(path.glob("*.md"))
    if not section_paths:
        fail(f"{path} must contain at least one `NN-section-slug.md` file")

    seen_numbers: set[str] = set()
    for section_path in section_paths:
        match = SECTION_RE.match(section_path.name)
        if not match:
            fail(f"{section_path} must be named like `01-introduction.md`")
        number = match.group(1)
        if number in seen_numbers:
            fail(f"{path} contains duplicate section number `{number}`")
        seen_numbers.add(number)

    body = "\n\n".join(section_path.read_text(encoding="utf-8").strip() for section_path in section_paths)
    return section_paths, body + "\n"


def load_paper(path: Path) -> Paper:
    config_path = path / "config.yaml"
    if not config_path.exists():
        fail(f"{path} must contain config.yaml")

    data = load_yaml(config_path)
    title = require_string(data, "title", path)
    slug = require_string(data, "slug", path)
    status = require_string(data, "status", path)
    summary = require_string(data, "summary", path)
    published_at, published_at_raw, display_date = parse_published_at(data, config_path)

    expected_slug = path.name
    if slug != expected_slug:
        fail(f"{config_path} has slug `{slug}`, but directory requires `{expected_slug}`")
    if not SLUG_RE.match(slug):
        fail(f"{config_path} slug `{slug}` must use lowercase kebab-case")

    tags = data.get("tags")
    if not isinstance(tags, list) or not tags:
        fail(f"{path} must define a non-empty `tags` list")
    clean_tags = []
    for tag in tags:
        if not isinstance(tag, str) or not tag.strip():
            fail(f"{config_path} tags must be non-empty strings")
        tag = tag.strip()
        if tag not in TAG_LABELS:
            fail(f"{config_path} uses unknown tag `{tag}`")
        clean_tags.append(tag)

    section_paths, body = load_sections(path)
    html = markdown.markdown(
        body,
        extensions=["extra", "smarty", "toc"],
        output_format="html5",
    )

    return Paper(
        title=title,
        slug=slug,
        published_at=published_at,
        published_at_raw=published_at_raw,
        display_date=display_date,
        status=status,
        tags=clean_tags,
        tag_items=[{"slug": tag, "label": TAG_LABELS[tag]} for tag in clean_tags],
        summary=summary,
        source_path=path,
        section_paths=section_paths,
        content_markdown=body,
        content_html=html,
    )


def load_papers() -> list[Paper]:
    if not LIBRARY.exists():
        fail(f"missing source directory {LIBRARY}")

    loose_markdown = sorted(LIBRARY.glob("*.md"))
    if loose_markdown:
        fail("whitepapers must use directory layout: `library/whitepapers/{slug}/config.yaml` plus `NN-section.md` files")

    papers = [load_paper(path) for path in sorted(LIBRARY.iterdir()) if path.is_dir()]
    slugs = [paper.slug for paper in papers]
    if len(slugs) != len(set(slugs)):
        fail("duplicate whitepaper slugs detected")
    return sorted(papers, key=lambda paper: paper.published_at, reverse=True)


def render_site(papers: list[Paper]) -> None:
    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html", "j2"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    index_template = env.get_template("index.html.j2")
    paper_template = env.get_template("whitepaper.html.j2")

    featured_tags = [{"slug": tag, "label": TAG_LABELS[tag]} for tag in FEATURED_TAGS]

    (ROOT / "index.html").write_text(
        index_template.render(
            title="Steven Horton | AppSec Whitepapers",
            description="Steven Horton publishes whitepapers on proof-driven application security, static analysis, AI-assisted review, and secure software engineering.",
            site_root="./",
            asset_prefix="./",
            papers=papers,
            featured_tags=featured_tags,
        ),
        encoding="utf-8",
    )

    for paper in papers:
        out_dir = PUBLIC_WHITEPAPERS / paper.slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(
            paper_template.render(
                title=f"{paper.title} | Steven Horton",
                description=paper.summary,
                site_root="../../",
                asset_prefix="../../",
                paper=paper,
                content_html=paper.content_html,
            ),
            encoding="utf-8",
        )


def render_pdfs(papers: list[Paper]) -> None:
    try:
        from weasyprint import HTML
    except ImportError:
        fail("WeasyPrint is required for PDF generation. Install dependencies with `python3 -m venv .venv` then `.venv/bin/pip install -r requirements.txt`.")

    DIST_WHITEPAPERS.mkdir(parents=True, exist_ok=True)
    for paper in papers:
        html_path = PUBLIC_WHITEPAPERS / paper.slug / "index.html"
        pdf_path = DIST_WHITEPAPERS / f"{paper.slug}.pdf"
        HTML(filename=html_path).write_pdf(pdf_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the GitHub Pages whitepaper site.")
    parser.add_argument("--no-pdf", action="store_true", help="Render HTML only.")
    args = parser.parse_args()

    papers = load_papers()
    render_site(papers)
    if not args.no_pdf:
        render_pdfs(papers)

    print(f"Generated {len(papers)} whitepaper(s).")


if __name__ == "__main__":
    main()
