import streamlit as st
import re

st.set_page_config(page_title="LinkedIn Formatter", layout="wide")

# --- FORMATTERS ---
def to_bold(text, style="math"):
    bold_map = {
        "math": (0x1D400, 0x1D41A, "A", "a"),
        "fullwidth": (0xFF21, 0xFF41, "A", "a"),
    }

    upper_base, lower_base, upper_start, lower_start = bold_map.get(style, bold_map["math"])
    return ''.join([
        chr(upper_base + ord(c) - ord(upper_start)) if c.isupper() else
        chr(lower_base + ord(c) - ord(lower_start)) if c.islower() else
        c for c in text
    ])

def to_italic(text):
    italic_map = {
        'A': 0x1D434, 'B': 0x1D435, 'C': 0x1D436, 'D': 0x1D437, 'E': 0x1D438,
        'F': 0x1D439, 'G': 0x1D43A, 'H': 0x1D43B, 'I': 0x1D43C, 'J': 0x1D43D,
        'K': 0x1D43E, 'L': 0x1D43F, 'M': 0x1D440, 'N': 0x1D441, 'O': 0x1D442,
        'P': 0x1D443, 'Q': 0x1D444, 'R': 0x1D445, 'S': 0x1D446, 'T': 0x1D447,
        'U': 0x1D448, 'V': 0x1D449, 'W': 0x1D44A, 'X': 0x1D44B, 'Y': 0x1D44C, 'Z': 0x1D44D,
        'a': 0x1D44E, 'b': 0x1D44F, 'c': 0x1D450, 'd': 0x1D451, 'e': 0x1D452,
        'f': 0x1D453, 'g': 0x1D454, 'h': 0x210E, 'i': 0x1D456, 'j': 0x1D457,
        'k': 0x1D458, 'l': 0x1D459, 'm': 0x1D45A, 'n': 0x1D45B, 'o': 0x1D45C,
        'p': 0x1D45D, 'q': 0x1D45E, 'r': 0x1D45F, 's': 0x1D460, 't': 0x1D461,
        'u': 0x1D462, 'v': 0x1D463, 'w': 0x1D464, 'x': 0x1D465, 'y': 0x1D466, 'z': 0x1D467,
    }
    return ''.join([chr(italic_map[c]) if c in italic_map else c for c in text])

def to_underline(text):
    return ''.join(c + '\u0332' if c != ' ' else ' ' for c in text)

def extract_links(text):
    url_regex = r"(https?://[^\s]+)"
    return re.sub(url_regex, r"[\1](\1)", text)

def insert_emojis(text):
    emoji_map = {
        ":)": "😊", ":(": "😔", ":fire:": "🔥", ":star:": "⭐",
        ":check:": "✅", ":x:": "❌", ":sparkles:": "✨", ":rocket:": "🚀"
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

    if st.button("✍️ Convert to LinkedIn Style") and input_text.strip():
        linkedin_post = rewrite_to_linkedin_tone(input_text)
    else:
        linkedin_post = None

with right:
    st.markdown("### 👀 Formatted Preview")

    if input_text.strip():
        formatted = insert_emojis(input_text)
        formatted = extract_links(formatted)

        if format_type == "Bold":
            formatted = to_bold(formatted, style)
        elif format_type == "Italic":
            formatted = to_italic(formatted)
        elif format_type == "Underline":
            formatted = to_underline(formatted)

        st.text_area("📋 Copy Formatted Output", value=formatted, height=300)
        st.download_button("📥 Download", formatted, file_name=f"linkedin_post_{style.lower()}.txt")

        if linkedin_post:
            st.markdown("---")
            st.markdown("### 🤖 LinkedIn Style Rewrite")
            st.markdown(linkedin_post)
