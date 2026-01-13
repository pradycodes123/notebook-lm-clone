import os
from groq import Groq
from prompts import build_prompt

def analyze_text_with_groq(text: str) -> str:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = build_prompt(text)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=900
    )

    return response.choices[0].message.content
    