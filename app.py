# File: streamlit_app.py

import streamlit as st
from src.preprocess import clean_text
from src.vectorizer import get_vectors
from src.similarity import calculate_similarity

st.set_page_config(page_title="Plagiarism Checker", layout="centered")

st.title("📄 Assignment Plagiarism Checker")
st.markdown("Upload two text files to compare their similarity.")

uploaded_file1 = st.file_uploader("Upload Assignment 1 (.txt)", type=["txt"])
uploaded_file2 = st.file_uploader("Upload Assignment 2 (.txt)", type=["txt"])

if uploaded_file1 and uploaded_file2:
    # Read and decode
    text1 = uploaded_file1.read().decode("utf-8")
    text2 = uploaded_file2.read().decode("utf-8")

    # Preprocess
    clean1 = clean_text(text1)
    clean2 = clean_text(text2)

    # Vectorize
    vectors = get_vectors([clean1, clean2])

    # Similarity
    similarity = calculate_similarity(vectors[0], vectors[1])

    st.success(f"Similarity Score: **{similarity:.2f}%**")

    if similarity > 80:
        st.warning("⚠️ High similarity – possible plagiarism.")
    elif similarity > 50:
        st.info("🧐 Moderate similarity – review advised.")
    else:
        st.success("✅ Low similarity – likely original work.")
