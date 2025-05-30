
from PyPDF2 import PdfReader
from docx import Document

def read_file(path):
    if path.endswith(".txt"):
        with open(path, encoding="utf-8") as f:
            return f.read()
    elif path.endswith(".pdf"):
        return "\n".join([p.extract_text() or "" for p in PdfReader(path).pages])
    elif path.endswith(".docx"):
        return "\n".join([p.text for p in Document(path).paragraphs])
    return ""
