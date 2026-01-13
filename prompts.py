def build_prompt(text: str) -> str:
    return f"""
You are an academic assistant.

Tasks:
1. Write a concise summary in **5–7 bullet points only**
2. Each bullet must be **1–2 lines max**
3. Focus only on **definitions, syntax, and key concepts**
4. Create 5–6 quiz questions with short answers
5. Give exactly 3 YouTube search terms

Rules:
- Use only the provided text
- Be concise and technical
- Avoid repetition
- No paragraphs, bullets only for summary

Text:
{text}

Format strictly as Markdown:

### Summary
- point 1
- point 2

### Quiz
1. **Question:** ...
   **Answer:** ...
2. **Question:** ...
   **Answer:** ...

### YouTube Search Terms
1. Search Term 1
2. Search Term 2
3. Search Term 3
"""
