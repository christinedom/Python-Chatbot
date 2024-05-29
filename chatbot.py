from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

API_KEY = "YOUR_API_KEY_HERE"  # Replace this with your actual API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_route():
    user_input = request.json['userInput']
    response = chat.send_message(user_input)
    bot_message = response.text
    return jsonify({'response': bot_message})

if __name__ == '__main__':
    app.run(debug=True)