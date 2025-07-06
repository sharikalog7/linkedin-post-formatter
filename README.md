# LinkedIn Post Formatter

A Streamlit app to help you format LinkedIn posts with **bold**, *italic*, _underline_, emojis, and generate LinkedIn-style rewrites for better engagement.

---

## Features

- Convert text to bold using Unicode math or fullwidth styles  
- Faux italic and underline text styles  
- Automatically detect and format URLs  
- Insert common emojis from simple text codes  
- Generate LinkedIn-friendly rewrites with professional tone and call-to-action  
- Download formatted posts or copy to clipboard easily  

---

## Setup & Usage

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/linkedin-post-formatter.git
   cd linkedin-post-formatter
## Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Open the app in your browser (usually http://localhost:8501).


## Secrets & API Keys
This project does not commit any secrets like API keys to the repository.
To safely manage your OpenAI API key (or any other secrets):

Use .streamlit/secrets.toml locally (make sure it is added to .gitignore).

Use environment variables or secret managers in production.

Never commit .streamlit/secrets.toml or any secret file to git history.

## Removing Secrets from Git History
If you accidentally committed secrets, use the following steps to completely remove them:


   pip install git-filter-repo
   git filter-repo --path .streamlit/secrets.toml --invert-paths
   git push origin main --force


## Then revoke your exposed keys immediately.

Contributing
Feel free to submit issues or pull requests to improve the tool!

License
MIT License © Sharika Loganathan
