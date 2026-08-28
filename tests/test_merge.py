import sys
import tempfile
from pathlib import Path

from pypdf import PdfWriter

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from pdf_merge_cli.cli import merge


def _make_pdf(path: Path, pages: int) -> None:
    w = PdfWriter()
    for _ in range(pages):
        w.add_blank_page(width=72, height=72)
    with path.open("wb") as f:
        w.write(f)


def test_merge_combines_page_counts() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        a, b, out = tmp / "a.pdf", tmp / "b.pdf", tmp / "out.pdf"
        _make_pdf(a, 2)
        _make_pdf(b, 3)

        page_count = merge([a, b], out)

        assert page_count == 5
        assert out.exists()


if __name__ == "__main__":
    test_merge_combines_page_counts()
    print("ok")
