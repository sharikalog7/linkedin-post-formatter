import streamlit as st

st.set_page_config(page_title="LinkedIn Formatter", layout="centered")

# --- Unicode Formatters ---
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

def to_script_italic(text):
    return ''.join([chr(0x1D49C + ord(c) - 65) if c.isupper()
                    else chr(0x1D4B6 + ord(c) - 97) if c.islower()
                    else c for c in text])

def to_underline(text):
    return ''.join(c + '\u0332' for c in text)

# --- UI ---
st.title("🔤 LinkedIn Post Formatter")
st.caption("Format your LinkedIn post with stylish Unicode bold, italic, and underline.")

input_text = st.text_area("Paste your LinkedIn post here:", height=180)

format_option = st.radio("Choose formatting style:", ("Bold", "Italic", "Underline"))

bold_style = None
if format_option == "Bold":
    bold_style = st.selectbox("Choose bold style:", ("math", "fullwidth"))

formatted = ""
if input_text:
    if format_option == "Bold":
        formatted = to_bold(input_text, bold_style)
    elif format_option == "Italic":
        formatted = to_script_italic(input_text)
    elif format_option == "Underline":
        formatted = to_underline(input_text)

if formatted:
    st.markdown("### 🔎 Formatted Output:")
    st.code(formatted, language="markdown")

    st.download_button("📋 Copy Output", formatted, file_name="linkedin_formatted.txt")

st.markdown("---")
st.caption("Note: LinkedIn does not support rich HTML formatting. This tool uses Unicode-compatible styling.")
