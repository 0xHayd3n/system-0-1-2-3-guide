# Verification record

Prepared on **20 October 2026**. This record describes source and documentation checks. It is not scientific validation, author review, or replication.

## Source and scope

- Entire supplied Library attachment, `2503.06138v3.pdf`: all 1,840 extracted lines across 41 PDF pages read. Title page confirmed all six authors, arXiv:2503.06138v3, and 16 July 2025.
- Official [v3 record](https://arxiv.org/abs/2503.06138v3) checked for title, author order, revision date/time, subjects, DOI, under-review comment, and linked source license.
- Exact official [v3 PDF](https://arxiv.org/pdf/2503.06138v3) downloaded privately for visual inspection. Size: 4,456,971 bytes. SHA-256: `731e2ce3218a78e77c9f91b863d57ddc13fd722ab17747da8525263bbdd4cf4e`. All 41 pages confirmed.
- Visual review covered all five figures (PDF pages 9, 10, 15, 17, 22), Table 1 (page 20), and all numbered equations (page 18). Figure 4's reused-source credit and Figure 5's distinct axes checked.
- Equation 4's incomplete `q(o |)` occurs in the rendered official PDF. The CPC module labels further objective/expectation cautions as companion mathematical analysis, without inventing an author-issued correction.
- Attachment binary not materialized and binary equality to the official PDF not established. Matching version labels and page count are not asserted as a byte comparison.
- Source extraction, PDF and rendered pages remain outside the repository. No paper PDF, full text, or original figure is redistributed.

## Coverage and factual review

Six detailed modules cover the introduction, every background subsection, the complete framework and CPC discussion, all Bergsonian subsections, all discussion subsections, the conclusion, and a source map through acknowledgments and references. The map includes five figures, one table, eight numbered equations, and the reference span. There are no appendices in this source.

The review checked source pages, author list, evidence status, and the two explicit future comparisons in Section 5.1. It preserves the distinction between theoretical synthesis, mathematical formalization, philosophical interpretation, cited prior evidence, and proposed future tests. It also preserves the v3 consciousness qualification and avoids a universal numeric timing ladder.

The 24-entry claim index is an aid to navigation. The cited prior literature was not independently audited in full. The paper's hypotheses about societal free energy, collective consciousness, or embodiment-driven symbol systems were not tested here.

## Integrity checks

Run with Python 3:

```bash
python scripts/validate_repository.py
```

The offline checker validates required files, UTF-8 text, Markdown fences, local file links and anchors, exact v3 source pins, one-based PDF page ranges, citation author consistency, claim/source metadata, provenance fields and source-asset exclusions. The GitHub Actions workflow runs the same command on pushes and pull requests.

Preparation results:

- Offline checker passed across 22 repository files and 24 typed claims. All local links, anchors, citation author checks and exact-version checks passed.
- CITATION.cff parsed as YAML and validated against the official [CFF 1.2.0 JSON schema](https://raw.githubusercontent.com/citation-file-format/citation-file-format/1.2.0/schema.json).
- Ten distinct fixed public URLs in the documentation, metadata, license and checker attribution returned HTTP 200, including exact v3 record/PDF/HTML, source license, CC BY summary/legal code, DOI and format reference. The work-level DOI resolves to the unversioned record; factual reading links remain pinned to v3.
- The authenticated owner's repository inventory was checked twice before creation. No matching System 0/1/2/3 or quad-process guide was found. Only this v3 guide was prepared for publication.

None of these checks confirms the empirical validity of the paper.

## Publication checks

The public repository was created under `0xHayd3n/system-0-1-2-3-guide`, with `main` as its default branch, the versioned paper record as its homepage, and descriptive research topics.

Anonymous GitHub API requests confirmed `private: false` and `visibility: public`. The remote tree contained exactly the 22 tracked files. All 22 files were retrieved without credentials from public raw URLs and matched the local committed text after line-ending normalization. Remote `main` matched the local commit. No PDF, paper extraction, original figure, or archive was present.

The [initial publication workflow](https://github.com/0xHayd3n/system-0-1-2-3-guide/actions/runs/39386342559) completed successfully. It ran the same offline integrity checker on GitHub. Later edits run that workflow again; consult the repository's current check status for the latest commit.

This task created one repository for the exact updated v3 source. It did not create or publish an earlier-version repository. No requested action remains blocked.
