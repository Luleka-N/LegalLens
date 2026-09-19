from pypdf import PdfReader
import streamlit as st

st.title("LegalLens")
st.write("AI-powered Legal Document Analysis Tool")

uploaded_file = st.file_uploader(
    "Upload a contract",
    type=["pdf"] )

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    st.subheader("Contract Text")
    st.text_area("Extracted text", text, height=400)