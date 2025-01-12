import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

app = Flask(__name__)

# Function to read documents from a folder
def read_documents(folder_path):
    documents = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                documents[filename] = file.read()
    return documents

# Load documents into memory (you can also implement caching)
documents = read_documents(r'D:\Work\Codes\git repository\GenAI\Google Chatbot\documents')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    
    # Check if the user input can be answered by documents
    response_text = answer_from_documents(user_input) or answer_from_chatbot(user_input)
    return jsonify({'response': response_text})

def answer_from_documents(user_input):
    # Simple keyword search in documents (you can improve this with NLP techniques)
    for title, content in documents.items():
        if user_input.lower() in content.lower():
            return f"Found in {title}: {content[:200]}..."  # Return first 200 characters
    
    return None  # No answer found in documents

def answer_from_chatbot(user_input):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat()
    response = chat_session.send_message(user_input)
    
    return response.text

if __name__ == '__main__':
    app.run(debug=True)


'''
chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "hello",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hello! How can I help you today?\n",
      ],
    },
  ]
)

response = chat_session.send_message(input("User : "))
print(f"Chatbot : {response.text}")
'''