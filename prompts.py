def build_prompt(text: str) -> str:
    return f"""
You are an academic assistant.

Tasks:
1. Give a clear and a detailed summary - less than 1000 words
2. Create 8–10 quiz questions with answers
3. Give 3 YouTube search terms

Rules:
- Use only the provided text
- Do not add external knowledge
- Keep answers concise

Text:
{text[:3000]}

Format strictly as:

SUMMARY:
...

QUIZ:
Q1:
A1:
...

YOUTUBE:
1.
2.
3.
"""
