from flask import Flask, render_template_string, request
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()

# Chatbot HTML template with footer links
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Chatbot</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #74ebd5 0%, #9face6 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .chat-container {
            width: 500px;
            max-width: 95%;
            height: 85vh;
            background: #fff;
            border-radius: 16px;
            box-shadow: 0px 8px 30px rgba(0,0,0,0.2);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        .header {
            background: #007bff;
            color: white;
            text-align: center;
            padding: 15px;
            font-size: 20px;
            font-weight: bold;
            border-top-left-radius: 16px;
            border-top-right-radius: 16px;
        }
        .messages {
            flex: 1;
            padding: 15px;
            overflow-y: scroll;
            background: #f9fafc;
        }
        .messages::-webkit-scrollbar { width: 8px; }
        .messages::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 8px;
        }
        .messages::-webkit-scrollbar-thumb {
            background: #007bff;
            border-radius: 8px;
        }
        .messages::-webkit-scrollbar-thumb:hover {
            background: #0056b3;
        }
        .message {
            margin: 10px 0;
            padding: 12px 16px;
            border-radius: 20px;
            max-width: 75%;
            line-height: 1.5;
            word-wrap: break-word;
            animation: fadeIn 0.3s ease-in-out;
        }
        .user {
            background: #007bff;
            color: white;
            margin-left: auto;
            border-bottom-right-radius: 4px;
        }
        .bot {
            background: #e9ecef;
            color: #333;
            margin-right: auto;
            border-bottom-left-radius: 4px;
        }
        .input-container {
            display: flex;
            padding: 12px;
            border-top: 1px solid #ddd;
            background: #fff;
        }
        textarea {
            flex: 1;
            resize: none;
            padding: 12px;
            border-radius: 12px;
            border: 1px solid #ccc;
            font-size: 14px;
            outline: none;
        }
        button {
            margin-left: 10px;
            padding: 12px 20px;
            border: none;
            border-radius: 12px;
            background: #007bff;
            color: white;
            cursor: pointer;
            font-size: 14px;
            transition: 0.2s;
        }
        button:hover {
            background: #0056b3;
        }
        .footer {
            text-align: center;
            padding: 10px;
            background: #f1f1f1;
            border-top: 1px solid #ddd;
        }
        .footer a {
            margin: 0 10px;
            text-decoration: none;
            color: #007bff;
            font-weight: bold;
            transition: 0.2s;
        }
        .footer a:hover {
            color: #0056b3;
        }
        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(10px);}
            to {opacity: 1; transform: translateY(0);}
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="header">💬 Flask Chatbot</div>
        <div class="messages" id="messages">
            {% for chat in chats %}
                <div class="message user">{{ chat.user }}</div>
                <div class="message bot">{{ chat.bot }}</div>
            {% endfor %}
        </div>
        <form method="POST" class="input-container">
            <textarea name="prompt" rows="2" placeholder="Type your message..."></textarea>
            <button type="submit">Send</button>
        </form>
        <div class="footer">
            Connect with me: 
            <a href="https://www.linkedin.com/in/khalil-aulfat/" target="_blank">LinkedIn</a> |
            <a href="https://github.com/khalilulfat" target="_blank">GitHub</a>
        </div>
    </div>

    <script>
        // Auto-scroll to latest message
        var messagesDiv = document.getElementById("messages");
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    </script>
</body>
</html>
"""

# Store chat history in memory
chat_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_prompt = request.form.get("prompt")
        if user_prompt:
            response = client.responses.create(
                model="gpt-4o",
                input=user_prompt
            )
            bot_reply = response.output_text
            chat_history.append({"user": user_prompt, "bot": bot_reply})
    return render_template_string(html_template, chats=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
