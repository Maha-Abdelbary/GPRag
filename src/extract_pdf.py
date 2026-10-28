import json
import pymupdf

from config import RAW_PDF_DIR, EXTRACTED_TEXT_DIR


def extract_pdf(pdf_path):
    """Returns a list of pages: each has its number and text."""
    pages = []
    with pymupdf.open(pdf_path) as doc:
        for i, page in enumerate(doc, start=1):
            pages.append({"page": i, "text": page.get_text()})
    return pages


def main():
    pdfs = sorted(RAW_PDF_DIR.rglob("*.pdf"))
    if not pdfs:
        print("No PDF files found in", RAW_PDF_DIR)
        return

    EXTRACTED_TEXT_DIR.mkdir(parents=True, exist_ok=True)

    for pdf in pdfs:
        pages = extract_pdf(pdf)
        total_chars = sum(len(p["text"].strip()) for p in pages)
        empty_pages = sum(1 for p in pages if len(p["text"].strip()) < 20)

        data = {
            "source_file": pdf.name,
            "college": pdf.parent.name,
            "pages": pages,
        }

        json_path = EXTRACTED_TEXT_DIR / f"{pdf.stem}.json"
        json_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        txt_path = EXTRACTED_TEXT_DIR / f"{pdf.stem}.txt"
        with open(txt_path, "w", encoding="utf-8") as f:
            for p in pages:
                f.write(f"\n--- page {p['page']} ---\n{p['text']}\n")

        print(f"{pdf.name}: {len(pages)} pages | {total_chars} chars | empty pages: {empty_pages}")


if __name__ == "__main__":
    main()