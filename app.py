from flask import Flask, request, jsonify, render_template_string
import random

app = Flask(__name__)

# --- AI TEACHER ---
def ai_teacher(q):
    q = q.lower()
    if "malawi" in q: return "Capital of Malawi is Lilongwe! 🇲🇼"
    if "h2o" in q: return "H2O is Water - 2 Hydrogen + 1 Oxygen!"
    if "12x12" in q: return "12x12 = 144"
    if "photosynthesis" in q: return "Photosynthesis: Plants use sunlight + CO2 + Water to make food!"
    if "math" in q: return "Math is fun! Ask me any question like 15% of 200?"
    return f"AI Teacher: Great question about '{q}'! Keep studying - you're smart! 💪"

def quiz_gen(sub):
    bank = {
        "Maths": ["12x12=?", "15% of 200=?", "Solve: 2x+3=7", "What is 100/4?"],
        "Science": ["What is H2O?", "Capital of Malawi?", "What is Photosynthesis?", "How many planets?"],
        "English": ["Synonym of Happy?", "Past tense of Go?", "What is a noun?"]
    }
    return random.choice(bank.get(sub, ["What is the capital of Malawi?", "What is H2O?"]))

# --- WEBSITE ---
HTML = """
<!DOCTYPE html>
<html>
<head><title>Cash Net AI - Learn & Earn</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:Arial;background:#0f172a;color:white;padding:20px;text-align:center}
.card{background:#1e293b;padding:20px;border-radius:15px;margin:15px 0}
button{background:#22c55e;color:white;padding:12px 20px;border:none;border-radius:8px;font-weight:bold}
input{padding:12px;width:80%;border-radius:8px;border:none;margin:10px}
h1{color:#22c55e}
</style>
</head>
<body>
<h1>🚀 CASH NET AI IS LIVE!</h1>
<p>From Lilongwe to the World 🌍 - AI Learning Platform</p>

<div class="card">
<h3>🤖 AI Teacher</h3>
<input id="q" placeholder="Ask anything e.g. What is H2O?">
<br><button onclick="ask()">Ask AI</button>
<p id="ans"></p>
</div>

<div class="card">
<h3>📝 Quiz Generator</h3>
<button onclick="quiz()">Generate Quiz</button>
<p id="quiz"></p>
</div>

<div class="card">
<h3>💰 Coming Soon: Earn Features</h3>
<p>Paystack Payments | Premium Quizzes | Student Dashboard</p>
<button>Join Waitlist - MWK 5000/month</button>
</div>

<script>
async function ask(){
  let q=document.getElementById('q').value;
  let r=await fetch('/ask?q='+q);
  let d=await r.json();
  document.getElementById('ans').innerText=d.answer;
}
async function quiz(){
  let r=await fetch('/quiz?subject=Maths');
  let d=await r.json();
  document.getElementById('quiz').innerText=d.quiz;
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/ask')
def ask():
    q = request.args.get('q', '')
    return jsonify({"answer": ai_teacher(q)})

@app.route('/quiz')
def quiz_route():
    sub = request.args.get('subject', 'Maths')
    return jsonify({"quiz": quiz_gen(sub)})

if __name__ == '__main__':
    app.run()
