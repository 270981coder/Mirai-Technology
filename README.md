# Mirai-Technology

# 🎙️ Voice Notes to Flashcards

> **Transform your lecture recordings into structured study material using Generative AI.**

**Voice Notes to Flashcards** is an AI-powered educational application that converts lecture recordings and voice notes into useful study resources. Simply upload an audio recording, and the application uses **Google Gemini AI** to transcribe the lecture and generate a structured study guide, flashcards, and practice quiz.

---

## 🚀 Features

### 🎤 1. Audio Lecture Upload

Upload your lecture or voice-note recordings in common audio formats:

* `.wav`
* `.mp3`
* `.m4a`
* `.ogg`
* `.webm`

The uploaded audio can also be played directly inside the application.

### 📝 2. AI-Powered Transcription

Google Gemini AI converts the uploaded lecture recording into clear and readable text while preserving important technical terms and the original meaning.

### 📚 3. Automatic Study Guide

The application transforms the transcript into an exam-friendly study guide containing:

* Key Topics
* Important Concepts
* Definitions
* Key Points
* Formulas
* Quick Revision Summary

The AI is instructed to use information from the lecture transcript rather than introducing unrelated information.

### 🃏 4. AI-Generated Flashcards

The application automatically generates **8 study flashcards** based on the lecture.

Each flashcard contains:

* Question
* Answer

The flashcards focus on important concepts, definitions, formulas, and examples.

### 🧠 5. Practice Quiz

The application generates **5 multiple-choice questions** from the lecture transcript.

Each question includes:

* Question
* Four options — A, B, C, D
* Correct answer
* Short explanation

### 🖥️ 6. Interactive Streamlit Interface

All generated learning materials are organized into separate tabs:

* 📝 Transcript
* 📚 Study Guide
* 🃏 Flashcards
* 🧠 Quiz

---

## 🔄 How It Works

```text
🎙️ Upload Lecture Audio
          ↓
   🤖 Google Gemini AI
          ↓
     📝 Transcription
          ↓
   ┌──────┼─────────┐
   ↓      ↓         ↓
📚 Guide 🃏 Cards  🧠 Quiz
   ↓      ↓         ↓
        📖 Study
```

### Workflow

**Upload → Transcribe → Structure with AI → Generate Flashcards → Generate Quiz → Study**

---

## 🛠️ Tech Stack

| Technology            | Purpose                                 |
| --------------------- | --------------------------------------- |
| **Python**            | Core programming language               |
| **Streamlit**         | Web application interface               |
| **Google Gemini API** | AI transcription and content generation |
| **google-genai**      | Gemini API integration                  |
| **python-dotenv**     | Environment variable management         |
| **Generative AI**     | Study material generation               |

The project uses `streamlit`, `google-genai`, and `python-dotenv` as its main dependencies.

---

## 📁 Project Structure

```text
Mirai-Technology/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignored files
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/270981coder/Mirai-Technology.git
```

### 2. Navigate to the Project

```bash
cd Mirai-Technology
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> ⚠️ **Never commit your `.env` file or API key to GitHub.**

The application loads the Gemini API key from the environment and stops with an error if the key is missing.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 Example Use Case

Imagine you have a **45-minute Operating Systems lecture** recorded as an audio file.

Instead of manually listening to the entire lecture again:

```text
Lecture Recording
       ↓
AI Transcription
       ↓
Structured Study Guide
       ↓
8 Flashcards
       ↓
5 MCQ Questions
       ↓
Quick Revision
```

This makes the application useful for students preparing for:

* College examinations
* Class tests
* Viva examinations
* Technical interviews
* Competitive examinations
* Quick revision

---

## 🎯 Project Objectives

The main objectives of this project are:

* Reduce the time required to create study notes.
* Convert unstructured voice notes into structured learning material.
* Use Generative AI for personalized educational assistance.
* Make revision faster and more effective.
* Demonstrate practical integration of AI APIs into an application.
* Build an easy-to-use AI-powered educational tool.

---

## 🧠 AI Implementation

The project uses **Google Gemini 2.5 Flash** for multiple AI tasks, including:

1. Audio transcription
2. Study guide generation
3. Flashcard generation
4. Quiz generation

The application uses separate prompts for each task to control the format and content of the generated learning material.

---

## 🔐 Environment Variables

The application requires:

```env
GEMINI_API_KEY=your_api_key
```

Keep your API credentials private and never upload them to your public repository.

---

## 🌟 Future Improvements

Potential future enhancements include:

* 🎙️ Direct microphone recording
* 📄 PDF export of study guides
* 📥 Downloadable flashcards
* 📊 Quiz score tracking
* 👤 User authentication
* 💾 Saving previous lectures
* 🌐 Multi-language transcription
* 🔊 Text-to-speech study mode
* 📈 Student learning analytics
* ☁️ Cloud deployment
* 📱 Mobile-friendly interface

---

## 🎓 Skills Demonstrated

This project demonstrates practical experience in:

* Python development
* Streamlit application development
* Generative AI
* Google Gemini API integration
* Prompt engineering
* Speech-to-text processing
* AI-powered content generation
* Educational technology
* Environment variable management
* Git & GitHub

---

## 👨‍💻 Author

**Dhanraj Kumar**

GitHub:
https://github.com/270981coder

Project Repository:
https://github.com/270981coder/Mirai-Technology

---

## 📜 License

This project is intended for educational and learning purposes.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**Made with Python, Streamlit & Google Gemini AI.** 🤖📚
