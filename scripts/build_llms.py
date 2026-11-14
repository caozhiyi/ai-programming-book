#!/usr/bin/env python3
"""Build llms.txt / llms-full.txt for AI crawlers (llmstxt.org convention).

Usage:
    python scripts/build_llms.py SITE_DIR [MKDOCS_YML]

Reads site_name/site_url/site_description/repo_url/nav from the mkdocs
config plus docs_dir, then writes:
    SITE_DIR/llms.txt       curated index, one line per chapter
    SITE_DIR/llms-full.txt  full book concatenated in nav order

Works for both the Chinese site (mkdocs.yml) and the English site
(mkdocs.en.yml) — everything is derived from the given config.
"""
import re
import sys
import pathlib
import urllib.parse

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


class _L(yaml.SafeLoader):
    """SafeLoader that tolerates mkdocs' !!python/name: tags."""

    pass


_L.add_multi_constructor(
    "tag:yaml.org,2002:python/name:",
    lambda loader, suffix, node: suffix,
)


def load_yaml(path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=_L)


def iter_nav(nav):
    """Yield (kind, title, value): kind in {'section', 'page'}."""
    for item in nav:
        if isinstance(item, str):
            yield "page", None, item
            continue
        (title, val), = item.items()
        if isinstance(val, list):
            yield "section", title, val
        else:
            yield "page", title, val


def build(cfg, docs_dir):
    site = cfg["site_url"]
    site_name = cfg["site_name"]
    desc = cfg.get("site_description", "")
    repo = cfg.get("repo_url", "")
    lang = cfg.get("theme", {}).get("language", "zh")

    def load_meta(rel):
        raw = (docs_dir / rel).read_text(encoding="utf-8")
        m = FM_RE.match(raw)
        meta = load_yaml_text(m.group(1)) if m else {}
        return meta or {}, (raw[m.end():] if m else raw)

    def load_yaml_text(text):
        try:
            return yaml.load(text, Loader=_L) or {}
        except yaml.YAMLError:
            return {}

    def page_url(rel):
        slug = rel.rsplit(".", 1)[0]
        if slug == "index":
            return site
        return site + urllib.parse.quote(slug) + "/"

    def chapter_title(meta, nav_title, rel):
        return meta.get("seo_title") or meta.get("title") or nav_title or pathlib.Path(rel).stem

    zh = lang.startswith("zh")
    read_label = "在线阅读" if zh else "Read online"
    idx = [
        f"# {site_name}",
        "",
        f"> {desc}",
        "",
        "## 基本信息" if zh else "## Overview",
        "",
        f"- {read_label}: {site}",
    ]
    if repo:
        idx.append(f"- GitHub 源码: {repo}" if lang.startswith("zh") else f"- GitHub repository: {repo}")
    idx += [f"- Language: {'简体中文' if lang.startswith('zh') else 'English'}", "", "## 全书目录" if lang.startswith("zh") else "## Table of Contents"]

    full = [f"# {site_name}", "", f"> {desc}"]
    if repo:
        full.append(f"- Source: {repo}")

    def walk(items, depth):
        nonlocal idx, full
        for kind, title, val in iter_nav(items):
            if kind == "section":
                head = f"{'#' * (depth + 2)} {title}"
                idx += ["", head]
                full += ["", f"{'#' * (depth + 1)} {title}"]
                walk(val, depth + 1)
                continue
            meta, body = load_meta(val)
            t = chapter_title(meta, title, val)
            url = page_url(val)
            d = meta.get("description")
            idx.append(f"- [{t}]({url}): {d}" if d else f"- [{t}]({url})")
            full += ["", f"{'#' * (depth + 2)} {t}", "", f"[{url}]", "", body.rstrip()]

    walk(cfg["nav"], 1)
    return "\n".join(idx) + "\n", "\n".join(full) + "\n"


def main():
    out_dir = pathlib.Path(sys.argv[1])
    cfg_file = ROOT / (sys.argv[2] if len(sys.argv) > 2 else "mkdocs.yml")
    cfg = load_yaml(cfg_file)
    docs_dir = ROOT / cfg.get("docs_dir", "docs")
    idx, full = build(cfg, docs_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "llms.txt").write_text(idx, encoding="utf-8")
    (out_dir / "llms-full.txt").write_text(full, encoding="utf-8")
    print(f"{cfg_file.name} -> {out_dir}: llms.txt {len(idx)//1024}KB, llms-full.txt {len(full)//1024}KB")


if __name__ == "__main__":
    main()
