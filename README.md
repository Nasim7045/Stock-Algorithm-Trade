# 📊 PDF Investor Call Analyzer using Google Gemini API

This project automatically analyzes investor call transcripts in PDF format and generates a **concise financial summary** with a focus on:

- ✅ Trade-related updates  
- ✅ Strategic decisions  
- ✅ Sentiment and future guidance  
- ✅ Revenue and expansion highlights  

It uses **Google's Gemini API** to generate summaries and combines them into a final insightful report.

---

## 🚀 Features

- Extracts raw text from PDF investor call files
- Splits large content into manageable chunks
- Uses **Gemini Pro** (`models/gemini-pro`) to generate summaries
- Merges all summaries into a final report
- Handles large documents and long transcripts smoothly
- CLI-based with clean output
- Option to customize prompts

---

## 🧠 How It Works

1. Extracts all text from a PDF using `PyMuPDF`
2. Splits the text into 800-token chunks
3. Sends each chunk to Gemini with a focused prompt
4. Collects summaries and combines them into a final result

---

## 📦 Dependencies

Install the required packages via pip:

```bash
pip install google-generativeai PyMuPDF
🔑 Gemini API Setup
Visit Google AI Studio
Create a project and get your free Gemini API key
Replace "YOUR_FREE_API_KEY_HERE" in the script with your actual API key
python
Copy
Edit
genai.configure(api_key="YOUR_FREE_API_KEY_HERE")
📁 File Structure
vbnet
Copy
Edit
📦project-directory
 ┣ 📄 Trade-Change.py
 ┣ 📄 requirements.txt
 ┣ 📄 README.md
 ┗ 📄 SJS Transcript Call.pdf
📝 Usage
bash
Copy
Edit
python Trade-Change.py
Make sure to update the path in the script:

python
Copy
Edit
pdf_path = r"D:\Python Projects 2025\SJS Transcript Call.pdf"
📄 Sample Output
markdown
Copy
Edit
📄 FINAL SUMMARY:

**Final Summary: SJS Enterprises Investor Call**

- Walter Pack acquisition completed, transformative to future growth.
- Plans for deeper penetration into passenger vehicles & appliances.
- Export revenue nearly doubled YoY.
- New clients: Toyota Tsusho, Autoliv, Foxconn.
- Strategic expansion into North America and Europe...
...
🛠 Customization
You can tweak the prompt in analyze_chunks() and combine_summaries() functions to fit:

Technical analysis
Sentiment detection
Risk evaluation
Custom domains (healthcare, legal, education, etc.)
📬 Future Improvements
Add Streamlit-based web interface
Auto email the summary
Export to PDF or Excel
Integrate upload support
📃 License
MIT License – free for personal and commercial use

🙋‍♂️ Author
Developed by [Nasim Khan]
💼 Computer Engineer | AI Developer | Cloud & Security Enthusiast | Cyber Security & Network Engineer
📧 Email: nasimk7045@outlook.com

---
