# # utils.py

# def chunk_text(text, max_length=500, filetype=None):
#     """
#     Splits text into chunks of roughly max_length characters (no overlap).
#     Handles large documents for embedding.

#     Args:
#         text (str): Full extracted text from the document.
#         max_length (int): Max length of each chunk.
#         filetype (str): Optional, "excel", "pdf", or "docx".

#     Returns:
#         List[str]: List of text chunks.
#     """
#     lines = [line.strip() for line in text.split("\n") if line.strip()]
#     chunks = []
#     current_chunk = []

#     for line in lines:
#         if sum(len(s) for s in current_chunk) + len(line) < max_length:
#             current_chunk.append(line)
#         else:
#             chunks.append(" ".join(current_chunk))
#             current_chunk = [line]

#     if current_chunk:
#         chunks.append(" ".join(current_chunk))

#     return chunks

# utils.py

def chunk_text(text, max_length=430, overlap=30, filetype=None):
    """
    Splits text into chunks of max_length characters with overlap (character-based).
    """
    text = text.replace('\n', ' ').strip()
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + max_length, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        if end == text_length:
            break
        start += max_length - overlap

    return chunks