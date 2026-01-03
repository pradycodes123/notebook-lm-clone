from pdf_parser import extract_text_from_pdf
from llm_client import analyze_text_with_groq
from utils import chunk_text


def main():
    pdf_path = input("Enter full PDF file path: ").strip()

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
    chunks = chunk_text(text)
    results = []

    for i, chunk in enumerate(chunks):
        print(f"Analyzing chunk {i+1}/{len(chunks)}")
        results.append(analyze_text_with_groq(chunk))

    final_output = "\n\n".join(results)

    print("\n" + "=" * 50)
    print(final_output)
    print("=" * 50)

    with open("analysis_result.txt", "w", encoding="utf-8") as f:
        f.write(final_output)

    print("\nResults saved to analysis_result.txt")

    


if __name__ == "__main__":
    main()
