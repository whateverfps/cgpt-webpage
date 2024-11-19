from flask import Flask, request, jsonify, render_template
import requests

# Your OpenAI API key
API_KEY = "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"

# OpenAI API endpoint
OPENAI_URL = "https://api.openai.com/v1/chat/completions"

app = Flask(__name__)

# Root route to serve the HTML interface
@app.route('/')
def index():
    return render_template("index.html")

# Chat route to handle API requests
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the user's message from the request
        user_message = request.json.get("message", "")

        # Construct the payload for OpenAI API
        payload = {
            "model": "gpt-3.5-turbo",  # Change to "gpt-4" if needed
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0.7
        }

        # Define headers for the API request
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        # Make the POST request to OpenAI API
        response = requests.post(OPENAI_URL, headers=headers, json=payload)

        # Check if the response was successful
        if response.status_code == 200:
            # Extract the assistant's reply
            assistant_message = response.json()["choices"][0]["message"]["content"]
            return jsonify({"response": assistant_message})
        else:
            return jsonify({"error": response.status_code, "details": response.text}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
