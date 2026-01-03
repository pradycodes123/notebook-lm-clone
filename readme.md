# AI Study Assistant for Technical PDFs

A simple Python tool that processes technical PDF documents and generates
section-wise summaries, quiz questions, and relevant YouTube study topics
using a Large Language Model (LLM).

This project is designed to be **reliable, easy to understand, and suitable
for large academic PDFs**.

---

## Features
- Extracts text from PDF files
- Splits large documents into manageable sections (chunk-based processing)
- Generates summaries and quiz questions per section
- Avoids token limit issues on large PDFs
- Clean, modular Python code

---

## Tech Stack
- Python
- PyPDF2 (PDF text extraction)
- Groq API (LLaMA 3.1 model)

---

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
setx GROQ_API_KEY "gsk_..."
