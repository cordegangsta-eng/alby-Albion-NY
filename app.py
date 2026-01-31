from flask import Flask, render_template, request
import os

app = Flask(__name__)

# --- Simple Home Route with Resources + Formspree form ---
@app.route('/')
def home():
    return """
    <body style="font-family: sans-serif; max-width: 700px; margin: 40px auto; padding: 20px; line-height: 1.6;">
        <h1>🏠 Alby: Albion Community Hub</h1>
        <p>The web version of Alby is officially online to help the Albion community.</p>

        <div style="background: #f4f4f4; padding: 15px; border-left: 5px solid #007bff;">
            <h3>🍎 Food & Immediate Needs</h3>
            <ul>
                <li><b>Albion Food Pantry:</b> 411 E. State St. (Mon-Fri)</li>
                <li><b>Community Kitchen:</b> Christ Church, Main St.</li>
            </ul>
        </div>

        <div style="background: #f4f4f4; padding: 15px; border-left: 5px solid #28a745; margin-top: 10px;">
            <h3>🏠 Housing & Utilities</h3>
            <ul>
                <li><b>PathStone:</b> (585) 589-7027</li>
                <li><b>HEAP/Social Services:</b> (585) 589-7000</li>
            </ul>
        </div>

        <p style="margin-top: 20px;"><i>More resources coming soon. Stay safe, Albion!</i></p>

        <hr />
        <h2>Need help? Submit a request</h2>
        <form id="helpForm">
            <div style="margin-bottom:8px;"><input name="name" placeholder="Your name" style="width:100%;padding:8px;" required></div>
            <div style="margin-bottom:8px;"><input name="phone" placeholder="Phone or contact" style="width:100%;padding:8px;"></div>
            <div style="margin-bottom:8px;"><select name="needs" style="width:100%;padding:8px;">
                <option>Food</option>
                <option>Housing</option>
                <option>Utilities</option>
                <option>Other</option>
            </select></div>
            <div style="margin-bottom:8px;"><textarea name="message" placeholder="Describe the need" style="width:100%;padding:8px;" required></textarea></div>
            <div><button type="submit" style="padding:10px 16px;background:#007bff;color:white;border:none;">Submit Help Request</button></div>
        </form>

        <script>
        document.getElementById('helpForm').addEventListener('submit', async function(e){
            e.preventDefault();
            const form = e.target;
            const data = {
                name: form.name.value,
                phone: form.phone.value,
                needs: form.needs.value,
                message: form.message.value
            };
            try {
                const resp = await fetch('https://formspree.io/f/meekblgl', {
                    method: 'POST',
                    headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                const j = await resp.json().catch(() => ({}));
                if (resp.ok) {
                    alert('Request submitted — thank you!');
                    form.reset();
                } else {
                    alert('Submit failed: ' + (j.error || 'unknown error'));
                }
            } catch (err) {
                alert('Submit failed: ' + err);
            }
        });
        </script>
    </body>
    """

# --- Database Init Stub ---
def init_db():
    # You can add your SQLite logic here later!
    pass

if __name__ == "__main__":
    init_db()
    # This part helps you test locally; Render uses Gunicorn instead
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)