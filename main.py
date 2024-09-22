import streamlit as st
from transformers import pipeline
from gtts import gTTS
import os

# Load the translation model
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-tw")

# Streamlit UI
st.title("English to Twi Translator with Voice Output")

# Get input from the user
text = st.text_input("Enter text in English:")

if st.button("Translate and Speak"):
    if text:
        # Perform translation
        translation = translator(text, max_length=100)[0]['translation_text']
        st.write("Translated Text (Twi):", translation)
        
        # Generate speech from translation
        tts = gTTS(text=translation, lang='tw', slow=False)
        tts.save("twi_audio.mp3")
        
        # Play audio
        audio_file = open("twi_audio.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")
        audio_file.close()
        
        # Optionally delete the file after playing
        os.remove("twi_audio.mp3")
