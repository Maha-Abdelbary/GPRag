from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_PDF_DIR = BASE_DIR / "data" / "raw_pdfs"
EXTRACTED_TEXT_DIR = BASE_DIR / "data" / "extracted_text"
CHROMA_DIR = BASE_DIR / "chroma_db"

CHUNK_SIZE = 600
CHUNK_OVERLAP = 100

EMBEDDING_MODEL = "BAAI/bge-m3"
COLLECTION_NAME = "regulations"
TOP_K = 4