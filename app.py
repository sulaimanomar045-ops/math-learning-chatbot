from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    # Logic for processing the message and returning a response
    response = {
        'message': f'You said: {user_message}'
    }
    return jsonify(response)

@app.route('/')
def index():
    # Serve a simple HTML interface
    return '''<html>
    <head><title>Math Learning Chatbot</title></head>
    <body>
        <h1>Math Learning Chatbot</h1>
        <p>Ask me anything about math!</p>
    </body>
</html>''' 

if __name__ == '__main__':
    app.run(debug=True)