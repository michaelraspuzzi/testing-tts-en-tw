import streamlit as st
from transformers import pipeline
from tts import TTS
import os

# Load the translation model for English to Twi translation
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-tw")

# Load the Asante Twi TTS model
tts_model_name = "tw_asante/openbible/vits"
tts = TTS(model_name=tts_model_name, progress_bar=False)

def generate_speech(text):
    # Generate speech from the Twi text using Coqui TTS
    tts.tts_to_file(text=text, speaker=tts.speakers[0], file_path="twi_audio.wav")
    return "twi_audio.wav"

# Streamlit UI
st.title("English to Asante Twi Translator with Voice Output")

# Get input from the user
text = st.text_input("Enter text in English:")

if st.button("Translate and Speak"):
    if text:
        # Perform translation
        translation = translator(text, max_length=100)[0]['translation_text']
        st.write("Translated Text (Asante Twi):", translation)
        
        # Generate speech from translation using Coqui TTS
        audio_file = generate_speech(translation)

        # Play audio in the app
        audio_file = open(audio_file, "rb")
        st.audio(audio_file.read(), format="audio/wav")
        audio_file.close()

        # Optionally delete the file after playing
        os.remove("twi_audio.wav")
