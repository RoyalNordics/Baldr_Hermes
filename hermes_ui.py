import streamlit as st
import os
from core.hermes_core import process_task

st.set_page_config(page_title="Hermes Panel", layout="centered")

st.title("🤖 Hermes Prompt Panel")

# Inputfelt til API-key
api_key = st.text_input("🔐 OpenAI API Key", type="password")
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

# Inputfelt til prompt
task_input = st.text_area("💬 Skriv din opgave til Hermes her:")

# Knap til at køre Hermes
if st.button("🚀 Kør Hermes"):
    if not api_key:
        st.warning("Indtast din API-nøgle først.")
    elif not task_input:
        st.warning("Skriv en opgave først.")
    else:
        result = process_task(task_input)
        st.success("✅ Hermes svarede:")
        st.code(result, language="text")