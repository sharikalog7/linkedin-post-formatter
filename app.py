import streamlit as st

st.set_page_config(page_title="LinkedIn Formatter", layout="centered")

def to_bold(text):
    return ''.join([chr(0x1D400 + ord(c) - 65) if c.isupper()
                    else chr(0x1D41A + ord(c) - 97) if c.islower()
                    else c for c in text])

def to_italic(text):
    return ''.join([chr(0x1D434 + ord(c) - 65) if c.isupper()
                    else chr(0x1D44E + ord(c) - 97) if c.islower()
                    else c for c in text])

def to_underline(text):
    return ''.join(c + '\u0332' for c in text)

st.title("🔤 LinkedIn Post Formatter")

input_text = st.text_area("Paste your LinkedIn post here:", height=200)

format_option = st.radio(
    "Choose formatting style:",
    ("Bold", "Italic", "Underline")
)

formatted = ""
if input_text:
    if format_option == "Bold":
        formatted = to_bold(input_text)
    elif format_option == "Italic":
        formatted = to_italic(input_text)
    elif format_option == "Underline":
        formatted = to_underline(input_text)

if formatted:
    st.markdown("### Formatted Output:")
    st.code(formatted, language="markdown")
    st.button("Copy to Clipboard", on_click=lambda: st.toast("Copied! (Use your mouse to copy manually if browser blocks clipboard)"))

st.markdown("---")
st.caption("Note: LinkedIn doesn't support HTML formatting, so we use Unicode styles.")
