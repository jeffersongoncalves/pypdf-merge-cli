import argparse
import sys
from pathlib import Path

from pypdf import PdfWriter


def merge(pdfs: list[Path], output: Path) -> int:
    writer = PdfWriter()
    for pdf in pdfs:
        writer.append(pdf)
    with output.open("wb") as f:
        writer.write(f)
    page_count = len(writer.pages)
    writer.close()
    return page_count


def main() -> None:
    parser = argparse.ArgumentParser(prog="pdfmerge", description="Merge multiple PDF files into one.")
    parser.add_argument("pdfs", type=Path, nargs="+", help="PDF files to merge, in order")
    parser.add_argument("-o", "--output", type=Path, default=Path("merged.pdf"), help="Output PDF path (default: merged.pdf)")
    args = parser.parse_args()

    missing = [p for p in args.pdfs if not p.exists()]
    if missing:
        sys.exit(f"error: not found: {', '.join(str(p) for p in missing)}")

    page_count = merge(args.pdfs, args.output)
    print(f"{args.output} ({page_count} pages, {args.output.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
