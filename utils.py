import re

def chunk_text(text, target_size=4000):
    """
    Splits text into chunks of approximately target_size characters,
    respecting word boundaries to avoid cutting words in half.
    """
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        # +1 for the space
        if current_length + len(word) + 1 > target_size and current_chunk:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0
        
        current_chunk.append(word)
        current_length += len(word) + 1

    if current_chunk:
        chunks.append(" ".join(current_chunk))
        
    return chunks

def format_markdown(result: str) -> str:
    """
    Clean up or format the LLM output if necessary.
    Since we optimized the prompt to return valid Markdown, we just return it mostly as-is.
    """
    return result.strip()

def youtube_links(result: str) -> str:
    """
    Detects lines that look like YouTube search terms and adds links.
    Expects lines in the 'YOUTUBE:' section to be like '1. Search Term'
    """
    lines = result.splitlines()
    formatted = []
    in_youtube_section = False

    for line in lines:
        stripped = line.strip()
        
        # Simple detection of the "YOUTUBE" section header
        if "youtube" in stripped.lower() and (stripped.endswith(":") or stripped.startswith("#")):
            in_youtube_section = True
            formatted.append(line)
            continue
        
        if in_youtube_section and stripped and stripped[0].isdigit() and "." in stripped:
            # It's likely a list item: "1. Python Tutorial"
            parts = stripped.split(".", 1)
            if len(parts) == 2:
                number = parts[0]
                title = parts[1].strip()
                # Create a search link
                query = title.replace(" ", "+")
                link = f"{number}. [{title}](https://www.youtube.com/results?search_query={query})"
                formatted.append(link)
            else:
                formatted.append(line)
        else:
            # If we hit an empty line or another header, we might be out of the section,
            # but usually YOUTUBE is the last section. 
            # If we encounter a new header (starts with #), stop processing as youtube links
            if stripped.startswith("#"):
                in_youtube_section = False
            formatted.append(line)

    return "\n".join(formatted)
