from flask import Flask, render_template, request
import os

app = Flask(__name__)

# --- Simple Home Route ---
@app.route('/')
def home():
    return "<h1>🏠 Alby: Albion Community Hub</h1><p>The web version of Alby is officially online!</p>"

# --- Database Init Stub ---
def init_db():
    # You can add your SQLite logic here later!
    pass

if __name__ == "__main__":
    init_db()
    # This part helps you test locally; Render uses Gunicorn instead
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)