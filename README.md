# pdf-merge-cli

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)

Tiny CLI to merge PDF files into one. Wraps [pypdf](https://pypi.org/project/pypdf/) (pure Python, no system dependencies).

## Install

```bash
pip install -e .
```

Requires Python 3.9+.

## Usage

```bash
pdfmerge a.pdf b.pdf c.pdf                  # writes merged.pdf
pdfmerge a.pdf b.pdf -o combined.pdf        # explicit output path
```

| Argument | Required | Description |
|---|---|---|
| `pdfs` | yes | PDF files to merge, in order (2 or more) |
| `-o`, `--output` | no | Output PDF path (default: `merged.pdf`) |

On success, prints the output path, page count, and file size:

```
merged.pdf (12 pages, 48213 bytes)
```

Exits non-zero with an error message if any input file doesn't exist.

## Development

```bash
pip install -e .
python tests/test_merge.py
```

## License

MIT © [Jefferson Gonçalves](https://github.com/jeffersongoncalves)
