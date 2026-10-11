from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🚀 CASH NET AI IS LIVE!</h1>
    <h2>From Lilongwe to World 🌍</h2>
    <p>AI Teacher Loading...</p>
    <p>Your site: cash-net-ai.onrender.com</p>
    <p style='color:green'><b>✅ Deployment SUCCESS!</b></p>
    """

if __name__ == '__main__':
    app.run()
