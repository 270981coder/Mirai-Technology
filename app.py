import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# ==========================================
# 1. Load Gemini API Key
# ==========================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API key not found. Please check your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)


# ==========================================
# 2. Page Configuration
# ==========================================

st.set_page_config(
    page_title="Voice Notes to Flashcards",
    page_icon="🎙️",
    layout="wide"
)


# ==========================================
# 3. Session State
# ==========================================

if "transcript" not in st.session_state:
    st.session_state.transcript = ""

if "study_guide" not in st.session_state:
    st.session_state.study_guide = ""

if "flashcards" not in st.session_state:
    st.session_state.flashcards = ""

if "quiz" not in st.session_state:
    st.session_state.quiz = ""    


# ==========================================
# 4. Application Header
# ==========================================

st.title("🎙️ Voice Notes to Flashcards")

st.subheader(
    "Speak your lecture notes. Let AI organize them for you."
)

st.write(
    "Upload your lecture recording and turn your chaotic "
    "voice notes into useful study material."
)

st.divider()


# ==========================================
# 5. Audio Upload
# ==========================================

st.header("🎤 Lecture Audio")

audio_file = st.file_uploader(
    "Upload your lecture audio",
    type=["wav", "mp3", "m4a", "ogg", "webm"],
    help="Upload your lecture or voice-note recording."
)


# ==========================================
# 6. Display Audio
# ==========================================

if audio_file is not None:

    st.success("✅ Audio uploaded successfully!")

    st.audio(
        audio_file,
        format=audio_file.type
    )

    st.write(f"**File:** {audio_file.name}")

    st.divider()


    # ======================================
    # 7. Process Lecture
    # ======================================

    if st.button(
        "🚀 Process Lecture",
        type="primary",
        use_container_width=True
    ):

        # ==================================
        # Transcription
        # ==================================

        with st.spinner(
            "🎧 Gemini is transcribing your lecture..."
        ):

            try:

                mime_type = audio_file.type

                # Fallback MIME type
                if not mime_type:

                    extension = (
                        audio_file.name
                        .lower()
                        .split(".")[-1]
                    )

                    mime_types = {
                        "mp3": "audio/mpeg",
                        "wav": "audio/wav",
                        "m4a": "audio/mp4",
                        "ogg": "audio/ogg",
                        "webm": "audio/webm"
                    }

                    mime_type = mime_types.get(
                        extension,
                        "audio/mpeg"
                    )

                # Upload audio to Gemini
                uploaded_file = client.files.upload(
                    file=audio_file,
                    config={
                        "mime_type": mime_type
                    }
                )

                # Ask Gemini to transcribe
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[
                        uploaded_file,
                        """
                        Transcribe this lecture audio accurately.

                        Instructions:
                        - Convert the spoken lecture into clear text.
                        - Preserve important technical terms.
                        - Do not summarize.
                        - Do not add information that was not spoken.
                        - Remove obvious filler words when possible.
                        - Keep the original meaning.
                        """
                    ]
                )

                transcript = response.text.strip()

                if not transcript:

                    st.error(
                        "❌ The transcription was empty. "
                        "Please try another audio recording."
                    )

                    st.stop()

                # Save transcript
                st.session_state.transcript = transcript

                st.success(
                    "✅ Lecture transcription completed!"
                )

            except Exception as e:

                st.error(
                    "❌ Something went wrong while "
                    "processing the audio."
                )

                st.caption(
                    f"Audio processing error: {str(e)}"
                )

                st.stop()


        # ==================================
        # Study Guide
        # ==================================

        with st.spinner(
            "📚 Gemini is creating your study guide..."
        ):

            study_prompt = f"""
You are an expert educational assistant.

The following is a student's chaotic lecture transcript.

Transform it into a clear, concise, exam-friendly
study guide.

IMPORTANT:
Use ONLY information present in the transcript.
Do not invent facts or add outside information.

LECTURE TRANSCRIPT:

{transcript}

Create the study guide using these sections:

# 📚 Study Guide

## Key Topics

List the major topics discussed.

## Important Concepts

Explain each important concept clearly and briefly.

## Definitions

List important terms and their definitions.

## Key Points

Give concise bullet points useful for revision.

## Formulas

Include important formulas ONLY if they appear
in the lecture.

If there are no formulas, write:

"No important formulas mentioned."

## Quick Revision

Give a short exam-focused summary.

Make the content accurate, concise,
and easy to understand.
"""

            try:

                guide_response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=study_prompt
                )

                study_guide = guide_response.text.strip()

                if study_guide:

                    st.session_state.study_guide = study_guide

                    st.success(
                        "📚 Study guide generated successfully!"
                    )

                else:

                    st.warning(
                        "⚠️ Gemini returned an empty study guide."
                    )

            except Exception as e:

                st.error(
                    "❌ Could not generate the study guide."
                )

                st.caption(
                    f"Study guide error: {str(e)}"
                )


        # ==================================
        # Flashcards
        # ==================================

        with st.spinner(
            "🃏 Gemini is creating flashcards..."
        ):

            flashcard_prompt = f"""
You are an expert educational assistant.

Create exactly 8 useful study flashcards
from the lecture transcript below.

IMPORTANT:
- Use ONLY information from the transcript.
- Do not add outside information.
- Focus on important concepts, definitions,
  formulas, and examples.
- Make the flashcards useful for exam preparation.

LECTURE TRANSCRIPT:

{transcript}

Return exactly 8 flashcards.

Use this format:

FLASHCARD 1
Question: ...
Answer: ...

FLASHCARD 2
Question: ...
Answer: ...

FLASHCARD 3
Question: ...
Answer: ...

FLASHCARD 4
Question: ...
Answer: ...

FLASHCARD 5
Question: ...
Answer: ...

FLASHCARD 6
Question: ...
Answer: ...

FLASHCARD 7
Question: ...
Answer: ...

FLASHCARD 8
Question: ...
Answer: ...
"""

            try:

                flashcard_response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=flashcard_prompt
                )

                flashcards = flashcard_response.text.strip()

                if flashcards:

                    st.session_state.flashcards = flashcards

                    st.success(
                        "🃏 Flashcards generated successfully!"
                    )

                else:

                    st.warning(
                        "⚠️ Gemini returned empty flashcards."
                    )

            except Exception as e:

                st.error(
                    "❌ Could not generate flashcards."
                )

                st.caption(
                    f"Flashcard error: {str(e)}"
                )


# ==========================================
# 8. Output Tabs
# ==========================================

st.divider()

st.header("📚 Your Study Materials")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📝 Transcript",
        "📚 Study Guide",
        "🃏 Flashcards",
        "🧠 Quiz"
    ]
)


# ==========================================
# Transcript Tab
# ==========================================

with tab1:

    if st.session_state.transcript:

        st.markdown(
            st.session_state.transcript
        )

    else:

        st.info(
            "📝 Your lecture transcript will appear here."
        )


# ==========================================
# Study Guide Tab
# ==========================================

with tab2:

    if st.session_state.study_guide:

        st.markdown(
            st.session_state.study_guide
        )

    else:

        st.info(
            "📚 Your AI-generated study guide "
            "will appear here."
        )


# ==========================================
# Flashcards Tab
# ==========================================

with tab3:

    if st.session_state.flashcards:

        st.markdown("### 🃏 Your Flashcards")

        st.markdown(
            st.session_state.flashcards
        )

    else:

        st.info(
            "🃏 Your flashcards will appear here "
            "after processing the lecture."
        )


# ==========================================
# Quiz Tab
# ==========================================

with tab4:

    if st.session_state.quiz:

        st.markdown("### 🧠 Practice Quiz")

        st.markdown(
            st.session_state.quiz
        )

    else:

        st.info(
            "🧠 Your 5-question quiz will appear here "
            "after processing the lecture."
        )


# ==================================
# Quiz Generation
# ==================================

with st.spinner(
    "🧠 Gemini is creating exactly 5 quiz questions..."
):
    quiz_transcript=st.session_state.transcript
    quiz_prompt = f"""
You are an expert educational assistant.

Create EXACTLY 5 multiple-choice questions from
the lecture transcript below.

IMPORTANT RULES:
- Use ONLY information from the transcript.
- Do not use outside knowledge.
- Generate exactly 5 questions.
- Each question must have exactly 4 options.
- Options must be A, B, C, and D.
- Include the correct answer.
- Include a short explanation.
- Questions should test understanding, not simple word matching.

LECTURE TRANSCRIPT:

{quiz_transcript}

Use this exact format:

QUESTION 1
Question: ...
A. ...
B. ...
C. ...
D. ...
Correct Answer: A
Explanation: ...

QUESTION 2
Question: ...
A. ...
B. ...
C. ...
D. ...
Correct Answer: B
Explanation: ...

QUESTION 3
Question: ...
A. ...
B. ...
C. ...
D. ...
Correct Answer: C
Explanation: ...

QUESTION 4
Question: ...
A. ...
B. ...
C. ...
D. ...
Correct Answer: D
Explanation: ...

QUESTION 5
Question: ...
A. ...
B. ...
C. ...
D. ...
Correct Answer: A
Explanation: ...
"""

    try:

        quiz_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=quiz_prompt
        )

        quiz = quiz_response.text.strip()

        if quiz:

            st.session_state.quiz = quiz

            st.success(
                "🧠 Exactly 5 quiz questions generated!"
            )

        else:

            st.warning(
                "⚠️ Gemini returned an empty quiz."
            )

    except Exception as e:

        st.error(
            "❌ Could not generate the quiz."
        )

        st.caption(
            f"Quiz error: {str(e)}"
        )    