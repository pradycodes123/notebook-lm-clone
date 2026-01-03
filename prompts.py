def build_prompt(text: str) -> str:
    return f"""
You are an academic assistant.

Tasks:
1. Write ONE clear, well-structured summary (max 1000 words)
2. Create 8–10 unique quiz questions with answers
3. Provide exactly 3 relevant YouTube search terms

Rules:
- Use only the provided text
- Do not repeat ideas or questions
- Do not add external information
- Keep language simple and technical
- Keep answers concise

Text:
{text}

Format strictly as:

SUMMARY:
<single combined summary>

QUIZ:
Q1:
A1:
Q2:
A2:
...

YOUTUBE:
1.
2.
3.
"""
def build_chunk_prompt(text: str) -> str:
    return f"""
You are an academic assistant.

Task:
- Extract concise technical notes as bullet points.
- Focus on definitions, rules, syntax, and examples.
- Do NOT write a summary.
- Do NOT create quiz questions.
- Do NOT give YouTube topics.

Rules:
- Use only the provided text.
- No repetition.
- Keep bullets short and factual.

Text:
{text}
"""
