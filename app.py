from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Alby: Albion Community Hub</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f4f4f9; margin: 0; padding: 0; color: #333; }
            .container { max-width: 600px; margin: 0 auto; background: white; min-height: 100vh; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            .header { background: #4b0082; color: white; padding: 25px 20px; text-align: center; }
            .header h1 { margin: 0; font-size: 28px; letter-spacing: 1px; }
            .header p { margin: 5px 0 0; opacity: 0.9; font-size: 14px; }
            .section { padding: 20px; border-bottom: 1px solid #eee; }
            h2 { font-size: 18px; color: #4b0082; margin-top: 0; border-left: 5px solid #ffd700; padding-left: 12px; margin-bottom: 15px; }
            .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
            .btn-emergency { background: #dc3545; color: white; text-align: center; padding: 12px; text-decoration: none; border-radius: 6px; font-weight: bold; display: block; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .btn-utility { background: #6c757d; color: white; text-align: center; padding: 12px; text-decoration: none; border-radius: 6px; font-size: 14px; display: block; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            ul { list-style: none; padding: 0; margin: 0; }
            li { background: #fff; border: 1px solid #e0e0e0; padding: 12px; margin-bottom: 8px; border-radius: 6px; }
            .date { font-weight: bold; color: #4b0082; font-size: 11px; text-transform: uppercase; display: block; margin-bottom: 4px; }
            form { background: #fafafa; padding: 15px; border-radius: 8px; border: 1px solid #eee; }
            input, select, textarea { width: 100%; padding: 12px; margin-bottom: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; font-size: 16px; }
            button { width: 100%; background: #4b0082; color: white; border: none; padding: 15px; font-size: 16px; font-weight: bold; border-radius: 4px; cursor: pointer; transition: background 0.2s; }
            button:hover { background: #3a0066; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🦅 Alby</h1>
                <p>Albion's Community Assistant</p>
            </div>

            <div class="section">
                <h2>🚨 Quick Contacts</h2>
                <div class="grid">
                    <a href="tel:911" class="btn-emergency">🚑 911 Emergency</a>
                    <a href="tel:5855895627" class="btn-emergency">👮 Albion Police</a>
                </div>
                <div class="grid" style="margin-top: 10px;">
                    <a href="tel:5855895527" class="btn-utility">Orleans Sheriff</a>
                    <a href="tel:8006424272" class="btn-utility">National Grid</a>
                </div>
            </div>

            <div class="section">
                <h2>📅 Community Calendar</h2>
                <ul>
                    <li><span class="date">Mon-Fri | 10am - 12pm</span><b>🍎 Albion Food Pantry</b><br><small>411 E. State St</small></li>
                    <li><span class="date">Check Website</span><b>📚 Hoag Library Tech Help</b><br><small>hoaglibrary.org</small></li>
                    <li><span class="date">2nd Wed of Month</span><b>🏛️ Village Board Meeting</b><br><small>Village Hall - 7 PM</small></li>
                </ul>
            </div>

            <div class="section">
                <h2>🤝 Local Resources</h2>
                <ul>
                    <li><b>🏠 PathStone:</b> (585) 589-7027</li>
                    <li><b>❄️ HEAP:</b> (585) 589-7000</li>
                    <li><b>🍲 Community Kitchen:</b> Christ Church, Main St.</li>
                </ul>
            </div>

            <div class="section">
                <h2>📨 Ask Alby for Help</h2>
                <form action="https://formspree.io/f/meekblgl" method="POST">
                    <input type="text" name="name" placeholder="Your Name" required>
                    <input type="text" name="contact" placeholder="Phone Number or Email" required>
                    <select name="need">
                        <option value="" disabled selected>What do you need help with?</option>
                        <option value="Food">Food / Groceries</option>
                        <option value="Housing">Housing / Heat</option>
                        <option value="Other">Other Question</option>
                    </select>
                    <textarea name="message" rows="4" placeholder="How can we help?" required></textarea>
                    <button type="submit">Send Request</button>
                </form>
            </div>

            <div style="text-align: center; padding: 30px 20px; color: #999; font-size: 12px; background: #f4f4f9;">
                &copy; 2026 Alby for Albion, NY.<br>
                Made with 💜 in Medina.
            </div>
        </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)