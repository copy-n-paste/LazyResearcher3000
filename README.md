# 🧠 LazyResearcher3000 – Because Thinking Is Overrated

Welcome to **LazyResearcher3000**, the AI-powered research assistant that generates a polished PDF report while you sip coffee, doomscroll, or wonder what day it is.

You just type in a topic (or vaguely grunt one out), and it:

* Thinks way harder than you ever will
* Summarizes history, current events, pros/cons, and more
* Slaps it into a beautifully formatted PDF with headers, a title page, and references
* Lets you take all the credit 🎓📄

> ⚠️ WARNING: May make you *look* more productive than you actually are.

---

## ✨ Features

✅ **Enter a Topic, Get a Full Report**
From “Artificial Intelligence” to “Why Pineapple on Pizza is a Crime” — it writes structured, sectioned content like a nerdy intern on Red Bull.

✅ **Cohere-Powered Brain**
Built using Cohere’s `command-r-plus` model, so it doesn’t just generate fluff — it generates *plausible* fluff.

✅ **PDFs That Don’t Look Like Trash**
Thanks to `reportlab`, your output won’t look like it was printed in Notepad. Headers! TOC! Page numbers!

✅ **Auto References**
Cites 5+ sources like it actually read them.

✅ **Custom Requirements? Sure.**
Want it to focus on “climate impact in Goa”? Just say so. It listens better than your group project teammates.

---

## 🛠 Requirements

* Python 3.7 or newer
* Install dependencies:

```bash
pip install -r requirements.txt
```

`requirements.txt`:

```
cohere
reportlab
requests
python-dotenv
```

---

## 🛠 Setup

1. **Clone this beautiful mess:**

```bash
git clone https://github.com/your-username/LazyResearcher3000.git
cd LazyResearcher3000
```

2. **Give it your secret key (Cohere API)**

Create a `.env` file:

```env
COHERE_API_KEY=your_actual_api_key_here
```

3. **Run it like a boss**

```bash
python main.py
```

Then follow the prompt. Like:

```
Enter the research topic: History of the Internet
Enter any specific requirements (or leave blank): Make it sound like a sci-fi movie
```

Boom — you get a PDF: `History_of_the_Internet_report.pdf`

---

## 📄 What’s in the Report?

* 🧢 Title page (so official it hurts)
* 📜 Table of Contents
* 🧩 Sections:

  * Introduction
  * History
  * Current Situation
  * Current Impact
  * Advantages
  * Disadvantages
  * Important Notes
  * New/Emerging Topics
  * Summary of Key Points
  * Conclusion
  * References (because academic guilt is real)

---

## 🤔 FAQ

**Q: Can I change the layout?**
Yes, in `pdf_generator.py`. Go wild. Add a watermark. Insert a cat emoji. You do you.

**Q: Is the content always 100% accurate?**
Nope. It’s an AI. Fact-check like a responsible human.

**Q: Can I replace Cohere with OpenAI or Gemini?**
Yes — if you’re feeling spicy. Just rework `research.py`.

---

## 🔮 Coming Soon (maybe, unless we get lazy)

* Export to DOCX or Markdown
* GUI version for mouse people
* Support for multiple LLMs
* Offline mode for when the Wi-Fi dies mid-cram

---

## 🙏 Credits

* **Cohere** – for the brain
* **ReportLab** – for the paper
* **Python** – for the vibes
* **You** – for trying to write papers the fun way

---

## 📢 Final Words

If it looks like you worked really hard on that 11-page report...
We won’t tell anyone you used `LazyResearcher3000`.

🢢🧠📄