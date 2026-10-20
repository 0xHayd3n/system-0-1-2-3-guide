# Contributing

Corrections that make the v3 paper easier to read and harder to misrepresent are welcome.

1. Locate the claim in this guide and the exact source in arXiv:2503.06138v3.
2. Include the paper section and one-based PDF page. Inspect rendered equations or figures before proposing detailed corrections.
3. Explain whether the issue concerns a source fact, interpretation, notation, coverage, attribution, or a broken link.
4. Keep original explanations. Do not upload the paper PDF, full text, original figures, or third-party code.
5. Update relevant metadata/claims.json entries and source maps with substantive changes.
6. Run `python scripts/validate_repository.py`; verify modified external links separately.

Preserve all six authors, the exact v3 pin, and the distinction between theoretical claims, cited prior support, future predictions, and companion analysis. Keep consciousness claims speculative where the paper does. Do not silently correct Equation 4 or claim an unqualified objective identity without showing the conventions involved.

This companion is not an implementation or a research-validation project. New experiments or later literature require clearly identified scope and evidence. Avoid presenting a documentation-check pass as scientific confirmation.

By contributing original material, you agree to license it under this repository's [CC BY 4.0 terms](LICENSE). Preserve third-party attribution and rights boundaries in [ATTRIBUTION.md](ATTRIBUTION.md).
