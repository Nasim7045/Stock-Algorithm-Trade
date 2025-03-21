import os
import fitz  # PyMuPDF
import google.generativeai as genai
from time import sleep


genai.configure(api_key="Gemini-Key")

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def split_text(text, max_tokens=800):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(current_chunk) >= max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def analyze_chunks(chunks):
    model = genai.GenerativeModel("models/gemini-2.0-flash") 
    summaries = []

    for i, chunk in enumerate(chunks):
        print(f"Analyzing chunk {i + 1}/{len(chunks)}...")
        prompt = (
            "You are a financial analyst AI. Summarize the following part of an investor call transcript. "
            "Focus on trade changes, decisions, sentiment, guidance, and any future plans mentioned:\n\n"
            + chunk
        )

        try:
            response = model.generate_content(prompt)
            summaries.append(response.text)
        except Exception as e:
            print(f"❌ Error analyzing chunk {i+1}: {e}")
            summaries.append("[Error in this chunk]")
        sleep(1)

    return summaries

def combine_summaries(summaries):
    full_summary = "\n\n".join(summaries)
    prompt = (
        "You are a financial analyst AI. Given the following summaries from an investor call, write a concise final summary focusing "
        "only on trade-related changes and strategic decisions (ignore Q&A):\n\n" + full_summary
    )

    model = genai.GenerativeModel("models/gemini-2.0-flash") 
    try:
        final_response = model.generate_content(prompt)
        return final_response.text
    except Exception as e:
        print(f"❌ Error generating final summary: {e}")
        return "[Final summary generation failed]"

def process_pdf_with_gemini(pdf_path):
    print("🔍 Analyzing PDF with Google Gemini...")
    text = extract_text_from_pdf(pdf_path)
    chunks = split_text(text)
    chunk_summaries = analyze_chunks(chunks)
    final_summary = combine_summaries(chunk_summaries)
    return final_summary


pdf_path = r"D:\Python Projects 2025\SJS Transcript Call.pdf"

summary = process_pdf_with_gemini(pdf_path)

print("\n📄 FINAL SUMMARY:\n")
print(summary)
