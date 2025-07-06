import streamlit as st
import re

st.set_page_config(page_title="LinkedIn Formatter", layout="wide")

# --- FORMATTERS ---
def to_bold(text, style="math"):
    if style == "math":
        return ''.join([chr(0x1D400 + ord(c) - 65) if c.isupper()
                        else chr(0x1D41A + ord(c) - 97) if c.islower()
                        else c for c in text])
    elif style == "fullwidth":
        return ''.join([chr(0xFF21 + ord(c) - 65) if c.isupper()
                        else chr(0xFF41 + ord(c) - 97) if c.islower()
                        else c for c in text])
    return text

def to_faux_italic(text):
    # Pseudo italic using soft diacritics (combining slash)
    return ''.join(c + '\u0357' if c.isalpha() else c for c in text)

def to_underline(text):
    return ''.join(c + '\u0332' for c in text)

def extract_links(text):
    url_regex = r"(https?://[^\s]+)"
    return re.sub(url_regex, r"[\1](\1)", text)

def insert_emojis(text):
    emoji_map = {
        ":)": "😊", ":(": "😔", ":fire:": "🔥", ":star:": "⭐", ":check:": "✅", ":x:": "❌"
    }
    for key, val in emoji_map.items():
        text = text.replace(key, val)
    return text

def rewrite_to_linkedin_tone(text):
    return f"""🚀 Here's how I'd rewrite this in a LinkedIn-friendly tone:

🔹 {text.capitalize().strip()}
🔹 Focused on value, clarity, and professional tone.
🔹 Add emojis, call-to-action, and personal voice.
"""

# --- LAYOUT ---
st.title("📝 LinkedIn Formatter Tool")
st.caption("Format your LinkedIn posts with **bold**, *italic*, _underline_, emojis, and generate LinkedIn-style rewrites.")

left, right = st.columns([2, 2])

with left:
    st.markdown("### ✍️ Paste Your Post")
    input_text = st.text_area("Paste your LinkedIn post here:", height=300)

    st.markdown("### 🎨 Style Options")
    style = st.selectbox("Font Style for Bold:", ["math", "fullwidth"])
    format_type = st.radio("Apply formatting to all text:", ["None", "Bold", "Italic", "Underline"])

    # Post transformation
    if st.button("✍️ Convert to LinkedIn Style"):
        linkedin_post = rewrite_to_linkedin_tone(input_text)
    else:
        linkedin_post = None

with right:
    st.markdown("### 👀 Formatted Preview")
    if input_text:
        formatted = insert_emojis(input_text)
        formatted = extract_links(formatted)

        if format_type == "Bold":
            formatted = to_bold(formatted, style)
        elif format_type == "Italic":
            formatted = to_faux_italic(formatted)
        elif format_type == "Underline":
            formatted = to_underline(formatted)

        st.code(formatted, language="markdown")
        st.download_button("📥 Download", formatted, file_name="linkedin_formatted.txt")
        st.text_area("📋 Copy Formatted Output", formatted, height=300)

        if linkedin_post:
            st.markdown("---")
            st.markdown("### 🤖 LinkedIn Style Rewrite")
            st.markdown(linkedin_post)
