from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Srinidhi Digital Solutions Chatbot is Running Successfully!"

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    # ఇది మన బాట్ ఇచ్చే ఆటోమేటిక్ రిప్లై
    reply = "నమస్కారం! శ్రీనిధి డిజిటల్ సొల్యూషన్స్ కి స్వాగతం. రైతులు, విద్యార్థులు, మరియు చిన్న వ్యాపారులకు సహాయం చేయడానికి నేను సిద్ధంగా ఉన్నాను. మీ ప్రశ్న అడగండి."
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
