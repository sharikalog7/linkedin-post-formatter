import streamlit as st
import re

st.set_page_config(page_title="LinkedIn Formatter", layout="centered")

# --- Formatters ---
def to_bold(text, style="math"):
    if style == "math":
        return ''.join([chr(0x1D400 + ord(c) - 65) if c.isupper()
                        else chr(0x1D41A + ord(c) - 97) if c.islower()
                        else c for c in text])
    elif style == "fullwidth":
        return ''.join([chr(0xFF21 + ord(c) - 65) if c.isupper()
                        else chr(0xFF41 + ord(c) - 97) if c.islower()
                        else c for c in text])
    else:
        return text

def to_faux_italic(text):
    # Simple slanted version with asterisks or soft diacritics
    return ''.join(c + '\u0357' if c.isalpha() else c for c in text)

def to_underline(text):
    return ''.join(c + '\u0332' for c in text)

def extract_and_linkify(text):
    # Converts plain URLs into markdown links
    url_regex = r"(https?://[^\s]+)"
    return re.sub(url_regex, r"[\1](\1)", text)

def insert_emojis(text):
    # Replace :) and :fire: with emoji
    emoji_map = {
        ":)": "😊",
        ":(": "😔",
        ":fire:": "🔥",
        ":star:": "⭐",
        ":check:": "✅",
        ":x:": "❌"
    }
    for key, val in emoji_map.items():
        text = text.replace(key, val)
    return text

# --- UI ---
st.title("🔤 LinkedIn Post Formatter")
st.caption("Bold, italic, underline, emojis, hyperlinks – all in one Unicode-safe tool for LinkedIn.")

input_text = st.text_area("📋 Paste your LinkedIn post below:", height=180)

# Formatting controls
format_option = st.radio("✨ Choose formatting style:", ("Bold", "Italic", "Underline", "None"))

bold_style = None
if format_option == "Bold":
    bold_style = st.selectbox("🅱️ Choose bold style:", ("math", "fullwidth"))

# Live processing
formatted = input_text
if formatted:
    formatted = insert_emojis(formatted)
    formatted = extract_and_linkify(formatted)

    if format_option == "Bold":
        formatted = to_bold(formatted, bold_style)
    elif format_option == "Italic":
        formatted = to_faux_italic(formatted)
    elif format_option == "Underline":
        formatted = to_underline(formatted)

# Display Output
if formatted.strip():
    st.markdown("### ✅ Formatted Output")
    st.code(formatted, language="markdown")

    st.download_button("📥 Download Formatted Text", formatted, file_name="linkedin_formatted.txt")

    st.markdown("### 👀 Realistic Preview")
    st.markdown(formatted)

st.markdown("---")
st.markdown("✅ Use our free **LinkedIn Text Formatter** to easily format your posts with **bold**, *italic*, __underline__, emojis, and [hyperlinks](https://linkedin.com).")


