from flask import Flask, request, jsonify
import random
app = Flask(__name__)

def ai_teacher(q):
    q=q.lower()
    if "malawi" in q: return "Capital of Malawi is Lilongwe!"
    if "h2o" in q: return "H2O is Water"
    if "12x12" in q: return "12x12 = 144"
    return "AI: Great question! Keep studying!"

def ai_gen(sub):
    bank={"Maths":["12x12=?","15% of 200=?"],"Science":["Red Planet?","H2O=?"],"English":["Noun is?"]}
    return random.choice(bank.get(sub, ["Capital of Malawi?"]))

@app.route("/")
def home():
    return """
    <h1>🎓 Cash net AI</h1>
    <p>AI Teacher is LIVE!</p>
    <a href='/ai/quiz/Maths'><button>Maths AI</button></a><br><br>
    <a href='/ai/quiz/Science'><button>Science AI</button></a><br><br>
    <a href='/ai/spin'><button>Spin</button></a><br><br>
    <a href='/ai/ask?q=What is H2O?'><button>Ask AI</button></a>
    """

@app.route("/ai/quiz/<subject>")
def quiz(subject): return jsonify({"question": ai_gen(subject)})
@app.route("/ai/ask")
def ask(): 
    q=request.args.get("q","")
    return jsonify({"answer": ai_teacher(q)})
@app.route("/ai/spin")
def spin(): return jsonify({"prize": random.choice(["K50","K100","K500"])})

app.run(host="0.0.0.0", port=81)
