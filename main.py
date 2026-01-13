from pdf_parser import extract_text_from_pdf
from llm_client import analyze_text_with_groq
from utils import chunk_text, format_markdown, youtube_links
import os

import tkinter as tk
from tkinter import filedialog
def main():
    # File picker popup
    root = tk.Tk()
    root.withdraw()
    pdf_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not pdf_path:
        print("No file selected.")
        return
    print("\nExtracting text from PDF...")
    try:
        text = extract_text_from_pdf(pdf_path)
    except Exception as e:
        print(f"Error: {e}")
        return
    if not text.strip():
        print("No readable text found.")
        return
    print("Analyzing with Groq...")
    chunks = chunk_text(text, target_size=4000)
    outputs = [
        "# AI Study Notes\n\nGenerated from selected PDF.\n\n---\n"
    ]
    
    total_chunks = len(chunks)
    for i, chunk in enumerate(chunks):
        print(f"Processing section {i+1}/{total_chunks} ({len(chunk)} chars)...")
        try:
            raw = analyze_text_with_groq(chunk)
            # The prompt now returns Markdown directly, but we still run it through
            # our lightweight formatters just in case/for links.
            result = format_markdown(raw)
            result = youtube_links(result)  

            outputs.append(f"""
## Section {i+1}
{result}
---
""")
        except Exception as e:
            print(f"Error processing chunk {i+1}: {e}")
            outputs.append(f"\n> [!WARNING]\n> Error processing section {i+1}: {e}\n")

    final_output = "\n".join(outputs)
    with open("analysis_result.md", "w", encoding="utf-8") as f:
        f.write(final_output)
    print(f"\nSuccess! Results saved to {os.path.abspath('analysis_result.md')}")
if __name__ == "__main__":
    main()
