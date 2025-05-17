import google.generativeai as genai
from chunk_text import extract_text_from_pdf, chunk_text # Called these functions from chunk_text.py

def setup_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-pro-latest')

def ask_gemini(model, prompt):
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    API_KEY = "##"  # API Key
    PDF_PATH = "/content/sample_data/llm.pdf"

    model = setup_gemini(API_KEY)
    text = extract_text_from_pdf(PDF_PATH)
    chunks = chunk_text(text, max_tokens=500)

    for i, chunk in enumerate(chunks):
        print(f"\n--- Gemini Output for Chunk {i+1} ---")
        response = ask_gemini(model, f"Summarize the following text:\n\n{chunk}")
        print(response)