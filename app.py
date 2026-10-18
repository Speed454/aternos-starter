from flask import Flask, render_template_string
from python_aternos import Client

app = Flask(__name__)

# Sənin kukin və server adın yerləşdirilib
ATERNOS_SESSION_COOKIE = "5QWnApVAlsV8Bh4YTq3LFYIWe5pT03GAvig66ShzTZAQ0NAM5iwN3GD7dGX24bscjfeX0NFbPI7HvTwv8JokkTaXbzNsQW3KsbDM"
SERVER_NAME = "156hardcore"

HTML_PAGE = """
<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8">
    <title>Server Başlatıcı</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 150px; background: #121212; color: white; }
        button { background: #ff5722; color: white; padding: 20px 40px; font-size: 24px; border: none; border-radius: 10px; cursor: pointer; }
        button:hover { background: #e64a19; }
    </style>
</head>
<body>
    <h1>156hardcore Serveri</h1>
    <p>Serveri işə salmaq üçün aşağıdakı düyməyə basın:</p>
    <form action="/start" method="post">
        <button type="submit">🚀 Serveri Aç</button>
    </form>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/start", methods=["POST"])
def start_server():
    try:
        account = Account(ATERNOS_SESSION_COOKIE)
        for srv in account.servers:
            if SERVER_NAME in srv.address:
                srv.start()
                break
        return "<h1 style='color:#4CAF50; text-align:center; margin-top:150px;'>Server açılır! 1-2 dəqiqəyə oyuna girə bilərsiniz.</h1>"
    except Exception as e:
        return f"<h1 style='color:#f44336; text-align:center;'>Xəta baş verdi: {e}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
