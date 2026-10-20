#!/usr/bin/env python3
"""Check companion integrity offline; this does not validate the research.

Adapted from 0xHayd3n/harness-learning-guide's documentation checker,
CC BY 4.0: https://github.com/0xHayd3n/harness-learning-guide/blob/main/scripts/validate_repository.py
This version adds v3, theory-scope and non-redistribution checks.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAPER_ID = "2503.06138"
PIN = PAPER_ID + "v3"
PDF_URL = "https://arxiv.org/pdf/" + PIN
EXPECTED_AUTHORS = [
    ("Tadahiro", "Taniguchi"), ("Yasushi", "Hirai"),
    ("Masahiro", "Suzuki"), ("Shingo", "Murata"),
    ("Takato", "Horii"), ("Kazutoshi", "Tanaka"),
]
REQUIRED = [
    "README.md", "AGENTS.md", "LLMS.txt", "ATTRIBUTION.md", "LICENSE",
    "CONTRIBUTING.md", "CITATION.cff", "VERIFICATION.md", "references/paper.bib",
    "metadata/paper.json", "metadata/claims.json", "metadata/sources.json",
    "docs/01-concepts-and-context.md",
    "docs/02-embodiment-and-individual-cognition.md",
    "docs/03-collective-predictive-coding.md",
    "docs/04-time-memory-and-canalization.md",
    "docs/05-implications-limitations-and-questions.md",
    "docs/06-paper-map.md", ".github/workflows/validate.yml",
]
CLAIM_KINDS = {
    "theoretical_proposal", "background_summary", "formalization",
    "philosophical_interpretation", "open_question",
}
ERRORS: list[str] = []
COUNTS = {"files": 0, "local_links": 0, "paper_page_links": 0, "external_links": 0, "claims": 0}


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def without_fences(text: str) -> str:
    lines, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
        elif fence is None:
            lines.append(line)
    return "\n".join(lines)


def anchors(text: str) -> set[str]:
    found: set[str] = set()
    duplicates: dict[str, int] = {}
    for line in without_fences(text).splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        title = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", match.group(1))
        title = re.sub(r"<[^>]+>", "", title).lower()
        base = "".join(ch for ch in title if ch.isalnum() or ch in "_- ").replace(" ", "-")
        occurrence = duplicates.get(base, 0)
        duplicates[base] = occurrence + 1
        found.add(base if occurrence == 0 else f"{base}-{occurrence}")
    found.update(re.findall(r'<a\s+(?:name|id)=["\']([^"\']+)', text))
    return found


def inspect_url(value: str, context: str, current: Path | None = None) -> None:
    parsed = urlsplit(value)
    if parsed.scheme:
        require(parsed.scheme in {"https", "http", "mailto"}, f"{context}: unexpected URL scheme {value}")
        COUNTS["external_links"] += 1
        if parsed.netloc.lower() in {"arxiv.org", "www.arxiv.org", "export.arxiv.org"} and PAPER_ID in parsed.path:
            require(parsed.path.rstrip("/") in {f"/{kind}/{PIN}" for kind in ["abs", "pdf", "html"]},
                    f"{context}: paper URL must pin exact v3: {value}")
            if parsed.path.startswith("/pdf/") and parsed.fragment:
                match = re.fullmatch(r"page=(\d+)", parsed.fragment)
                require(bool(match), f"{context}: invalid PDF page fragment {value}")
                if match:
                    require(1 <= int(match.group(1)) <= 41, f"{context}: out-of-range PDF page {value}")
                    COUNTS["paper_page_links"] += 1
        return
    require(not parsed.netloc, f"{context}: protocol-relative URL is unsupported: {value}")
    if current is None:
        return
    target = (current.parent / unquote(parsed.path)).resolve() if parsed.path else current
    try:
        target.relative_to(ROOT)
    except ValueError:
        ERRORS.append(f"{context}: local link escapes repository: {value}")
        return
    COUNTS["local_links"] += 1
    require(target.is_file(), f"{context}: missing local link {value}")
    if parsed.fragment and target.is_file():
        require(unquote(parsed.fragment) in anchors(target.read_text(encoding="utf-8")),
                f"{context}: missing local anchor {value}")


def inspect_json_urls(value: object, context: str) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            inspect_json_urls(item, f"{context}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            inspect_json_urls(item, f"{context}[{index}]")
    elif isinstance(value, str) and value.startswith(("http://", "https://")):
        inspect_url(value, context)


for name in REQUIRED:
    require((ROOT / name).is_file(), f"Missing required file: {name}")

files = [p for p in ROOT.rglob("*") if p.is_file()
         and not any(part in {".git", "__pycache__", ".venv"} for part in p.relative_to(ROOT).parts)]
for file in files:
    relative = str(file.relative_to(ROOT))
    COUNTS["files"] += 1
    require(file.suffix.lower() not in {".pdf", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".zip"},
            f"{relative}: source PDFs, image assets, and archives must not be redistributed")
    require(not file.name.lower().startswith(("_source", "source-library", "2503.06138")),
            f"{relative}: source extraction or paper file must stay outside the repository")
    try:
        text = file.read_text(encoding="utf-8")
    except UnicodeError:
        ERRORS.append(f"{relative}: not UTF-8 text")
        continue
    require("\ufffd" not in text, f"{relative}: replacement character")
    require(not any(ord(char) < 32 and char not in "\n\r\t" for char in text),
            f"{relative}: unexpected control character")
    require(not re.search(rf"https?://[^\s<>\"']*{re.escape(PAPER_ID)}v[12](?:\b|/)", text),
            f"{relative}: withdrawn paper-version URL")
    if file.suffix == ".md" or file.name == "LLMS.txt":
        fences = sum(bool(re.match(r"^\s*(`{3,}|~{3,})", line)) for line in text.splitlines())
        require(fences % 2 == 0, f"{relative}: unclosed code fence")
        visible = without_fences(text)
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)\s]+)\)", visible):
            inspect_url(target, relative, file)
        for target in re.findall(r"https?://[^\s<>\]\)\"']+", visible):
            if PAPER_ID in target:
                inspect_url(target.rstrip(".,;"), relative)

try:
    paper = json.loads((ROOT / "metadata/paper.json").read_text(encoding="utf-8"))
    claims = json.loads((ROOT / "metadata/claims.json").read_text(encoding="utf-8"))
    sources = json.loads((ROOT / "metadata/sources.json").read_text(encoding="utf-8"))
    for name, data in [("paper", paper), ("claims", claims), ("sources", sources)]:
        require(data.get("schema_version") == "1.0.0", f"{name}: unsupported schema version")
        inspect_json_urls(data, name)
    require([a["name"] for a in paper["authors"]] == [f"{g} {f}" for g, f in EXPECTED_AUTHORS],
            "Paper author order/content mismatch")
    require(paper["arxiv"]["id"] == PAPER_ID and paper["arxiv"]["version"] == "v3"
            and paper["arxiv"]["version_date"] == "2025-07-16",
            "Wrong paper ID, version, or version date")
    require(paper["page_count"] == 41, "Wrong paper page count")
    require(paper["license"]["spdx"] is None, "Do not assign a CC/SPDX license to the non-exclusive arXiv paper license")
    require("nonexclusive-distrib" in paper["license"]["url"], "Unexpected source license URL")
    require(paper["companion"]["experiments_run"] is False, "Companion research-scope mismatch")
    require(paper["companion"]["implementation_reproduced"] is False, "Companion implementation-scope mismatch")
    provenance = paper["provenance"]
    require(provenance["primary_source"] == "supplied_library_attachment_text", "Unexpected primary-source route")
    require(provenance["official_pdf_sha256"] == "731e2ce3218a78e77c9f91b863d57ddc13fd722ab17747da8525263bbdd4cf4e",
            "Official PDF digest mismatch")
    require(provenance["attachment_binary_equality_verified"] is False,
            "Attachment binary equality was not established")
    require(claims["paper_version"] == PIN, "Claims version mismatch")
    require(bool(claims["claims"]), "Empty claim index")
    claim_ids = [claim["id"] for claim in claims["claims"]]
    require(len(claim_ids) == len(set(claim_ids)), "Duplicate claim IDs")
    for claim in claims["claims"]:
        COUNTS["claims"] += 1
        require(claim["kind"] in CLAIM_KINDS, f"{claim['id']}: unknown claim kind")
        for field in ["statement", "scope", "caveat", "sources"]:
            require(bool(claim.get(field)), f"{claim['id']}: missing {field}")
        for source in claim["sources"]:
            require(bool(source["section"]), f"{claim['id']}: missing section")
            require(type(source["page"]) is int and 1 <= source["page"] <= 41, f"{claim['id']}: page out of range")
            require(source["url"] == f"{PDF_URL}#page={source['page']}", f"{claim['id']}: source page/URL mismatch")
    source_ids = [source["id"] for source in sources["sources"]]
    require(bool(source_ids) and len(source_ids) == len(set(source_ids)), "Missing or duplicate source IDs")
    bib = (ROOT / "references/paper.bib").read_text(encoding="utf-8")
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    require("cff-version: 1.2.0" in cff, "Missing CFF version")
    require("preferred-citation:" in cff, "Missing paper preferred citation")
    for given, family in EXPECTED_AUTHORS:
        require(f"{family}, {given}" in bib, f"BibTeX omits {given} {family}")
        require(f'given-names: "{given}"' in cff and f'family-names: "{family}"' in cff,
                f"CFF omits {given} {family}")
    require(PIN in bib and PIN in cff, "Citation version mismatch")
except (KeyError, TypeError, ValueError, OSError) as error:
    ERRORS.append(f"Metadata/citation integrity: {error}")

if ERRORS:
    print("\n".join(f"ERROR: {error}" for error in ERRORS))
    sys.exit(1)
print("PASS: " + ", ".join(f"{name}={value}" for name, value in COUNTS.items()))
print("Scope: UTF-8, required files, JSON/citation consistency, local anchors, v3 pins, PDF page ranges and redistribution guardrails.")
print("External reachability, full CFF schema, factual completeness and research validity require separate review.")
