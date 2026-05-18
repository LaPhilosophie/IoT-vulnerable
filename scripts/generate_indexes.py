#!/usr/bin/env python3
"""Generate repository indexes from the unified vulnerability summary."""

from __future__ import annotations

import os
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REPORTS = ROOT / "reports"
SUMMARY = DOCS / "VULNERABILITY_SUMMARY.md"

CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}", re.IGNORECASE)
CNVD_RE = re.compile(r"CNVD-\d{4}-\d+", re.IGNORECASE)
ID_RE = re.compile(r"(?:CVE-\d{4}-\d{4,7}|CNVD-\d{4}-\d+)", re.IGNORECASE)


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_table_separator(cells: list[str]) -> bool:
    return all(set(cell.replace(" ", "")) <= {":", "-"} for cell in cells)


def is_header_row(cells: list[str]) -> bool:
    text = " ".join(cells).lower()
    return (
        "vulnerable function" in text
        or "type of vulnerability" in text
        or "product / firmware" in text
        or "component" in text
    )


def parse_summary_tables(paths: list[Path]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for source in paths:
        if not source.exists():
            continue

        vendor = ""
        product = ""
        for raw_line in source.read_text(encoding="utf-8", errors="replace").splitlines():
            line = raw_line.strip()

            if line.startswith("## "):
                vendor = line.removeprefix("## ").strip()
                product = ""
                continue

            if not line.startswith("|"):
                continue

            cells = split_table_row(line)
            if len(cells) < 4 or is_table_separator(cells) or is_header_row(cells):
                continue

            first, component, identifier, vuln_type = cells[:4]
            if first:
                product = first

            rows.append(
                {
                    "vendor": vendor,
                    "product": product,
                    "component": component,
                    "identifier": identifier,
                    "type": vuln_type,
                }
            )

    return rows


def read_catalog_rows() -> list[dict[str, str]]:
    if not SUMMARY.exists():
        raise SystemExit(f"Missing summary source: {SUMMARY}")
    return parse_summary_tables([SUMMARY])


def markdown_link(label: str, target: Path) -> str:
    relative = Path(os.path.relpath(target, DOCS))
    if any(char.isspace() for char in str(relative)):
        return f"[{escape_cell(label)}](<{relative.as_posix()}>)"
    return f"[{escape_cell(label)}]({relative.as_posix()})"


def read_report_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for path in sorted(REPORTS.rglob("*.md")):
        relative = path.relative_to(REPORTS)
        parts = relative.parts
        if len(parts) < 4:
            continue

        category = parts[0]
        vendor = parts[1]
        product = "/".join(parts[2:-1])
        title = path.stem
        content = path.read_text(encoding="utf-8", errors="replace")
        identifiers = sorted(set(ID_RE.findall(content)), key=id_sort_key)

        rows.append(
            {
                "category": category,
                "vendor": vendor,
                "product": product,
                "report": title,
                "identifiers": ", ".join(identifier.upper() for identifier in identifiers),
                "path": markdown_link(title, path),
            }
        )

    return rows


def id_sort_key(identifier: str) -> tuple[str, int, int, str]:
    identifier = identifier.upper()
    match = re.match(r"([A-Z]+)-(\d{4})-(\d+)", identifier)
    if not match:
        return (identifier, 0, 0, identifier)
    prefix, year, number = match.groups()
    return (prefix, int(year), int(number), identifier)


def product_model(product: str) -> str:
    product = " ".join(product.split())
    product = re.sub(r"\s+Firmware\s+.*$", "", product, flags=re.IGNORECASE)
    product = re.sub(r"\s+[Vv]\d[\w.\-()]*.*$", "", product)
    product = re.sub(r"\s+B\d+\s+\d+(?:\.\d+)*$", "", product, flags=re.IGNORECASE)
    product = re.sub(r"\s+\d+(?:\.\d+)*(?:[A-Z]\d+)?(?:\s+BETA)?$", "", product, flags=re.IGNORECASE)
    if product.startswith("DIR-"):
        product = re.sub(r"\s+[A-Z]\d+$", "", product)
    return product.strip() or "Unknown"


def identifiers_from_row(row: dict[str, str], pattern: re.Pattern[str]) -> list[str]:
    return sorted({match.upper() for match in pattern.findall(row["identifier"])}, key=id_sort_key)


def write_table(path: Path, title: str, intro: str, headers: list[str], rows: list[list[str]]) -> None:
    lines = [
        f"# {title}",
        "",
        intro,
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]

    for row in rows:
        lines.append("| " + " | ".join(escape_cell(value) for value in row) + " |")

    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_report_index(report_rows: list[dict[str, str]]) -> None:
    table_rows = [
        [
            row["category"],
            row["vendor"],
            row["product"],
            row["report"],
            row["identifiers"],
            row["path"],
        ]
        for row in report_rows
    ]
    write_table(
        DOCS / "REPORT_INDEX.md",
        "Report Index",
        "File-level index for every Markdown vulnerability report under `reports/`.",
        ["Category", "Vendor", "Product Path", "Report", "Identifiers in File", "Path"],
        table_rows,
    )


def write_dataset_overview(catalog_rows: list[dict[str, str]], report_rows: list[dict[str, str]]) -> None:
    report_by_category = Counter(row["category"] for row in report_rows)
    report_by_vendor = Counter(row["vendor"] for row in report_rows)
    catalog_by_vendor = Counter(row["vendor"] for row in catalog_rows)
    cve_ids = sorted(
        {identifier for row in catalog_rows for identifier in identifiers_from_row(row, CVE_RE)},
        key=id_sort_key,
    )
    cnvd_ids = sorted(
        {identifier for row in catalog_rows for identifier in identifiers_from_row(row, CNVD_RE)},
        key=id_sort_key,
    )
    vendors = sorted({row["vendor"] for row in report_rows})
    products = {
        (row["category"], row["vendor"], row["product"].split("/")[0])
        for row in report_rows
    }

    lines = [
        "# Dataset Overview",
        "",
        "## Scope",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
        f"| Markdown vulnerability reports | {len(report_rows)} |",
        f"| Product/model directories | {len(products)} |",
        f"| Vendors | {len(vendors)} |",
        f"| Cataloged vulnerability entries | {len(catalog_rows)} |",
        f"| Unique CVE identifiers | {len(cve_ids)} |",
        f"| Unique CNVD identifiers | {len(cnvd_ids)} |",
        "",
        "## By Report Category",
        "",
        "| Category | Reports |",
        "| --- | ---: |",
    ]

    for category in sorted(report_by_category):
        lines.append(f"| {escape_cell(category)} | {report_by_category[category]} |")

    lines.extend(
        [
            "",
            "## By Vendor",
            "",
            "| Vendor | Reports | Catalog entries |",
            "| --- | ---: | ---: |",
        ]
    )

    for vendor in sorted(set(report_by_vendor) | set(catalog_by_vendor)):
        lines.append(f"| {escape_cell(vendor)} | {report_by_vendor[vendor]} | {catalog_by_vendor[vendor]} |")

    lines.append("")
    (DOCS / "DATASET_OVERVIEW.md").write_text("\n".join(lines), encoding="utf-8")


def write_readme(catalog_rows: list[dict[str, str]], report_rows: list[dict[str, str]]) -> None:
    cve_ids = {
        identifier
        for row in catalog_rows
        for identifier in identifiers_from_row(row, CVE_RE)
    }
    lines = [
        "# CVE-ID",
        "",
        f"This repository currently documents {len(catalog_rows)} vulnerability entries across {len(report_rows)} reports identified by our team.",
        "",
        f"{len(cve_ids)} unique CVE IDs have been confirmed.",
        "",
    ]

    for heading, pattern in [("CVE-ID", CVE_RE), ("CNVD-ID", CNVD_RE)]:
        grouped: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
        for row in catalog_rows:
            ids = identifiers_from_row(row, pattern)
            if not ids:
                continue
            grouped[row["vendor"]][product_model(row["product"])].update(ids)

        if not grouped:
            continue

        if heading != "CVE-ID":
            lines.extend(["", f"# {heading}", ""])

        for vendor in sorted(grouped):
            lines.extend([f"## {vendor}", ""])
            for model in sorted(grouped[vendor]):
                lines.extend([model, ""])
                for identifier in sorted(grouped[vendor][model], key=id_sort_key):
                    lines.append(f"- {identifier}")
                lines.append("")

    (ROOT / "README.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    catalog_rows = read_catalog_rows()
    report_rows = read_report_rows()

    write_report_index(report_rows)
    write_dataset_overview(catalog_rows, report_rows)
    write_readme(catalog_rows, report_rows)

    print(f"catalog_entries={len(catalog_rows)}")
    print(f"report_files={len(report_rows)}")


if __name__ == "__main__":
    main()
