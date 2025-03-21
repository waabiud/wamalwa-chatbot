from flask import Flask, render_template, request, jsonify
import aiml
import os

app = Flask(__name__)

# Initialize AIML Kernel
kernel = aiml.Kernel()

# Load or create bot brain
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    kernel.bootstrap(learnFiles="aiml_files/std-startup.xml", commands="load aiml b")
    kernel.saveBrain("bot_brain.brn")

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/ask", methods=['POST'])
def ask():
    message = request.form.get("messageText", "").strip()
    if not message:
        return jsonify({'status': 'ERROR', 'answer': "I didn't understand that!"})

    bot_response = kernel.respond(message)
    if not bot_response:
        bot_response = "I'm still learning. Can you rephrase?"

    return jsonify({'status': 'OK', 'answer': bot_response})

if __name__ == "__main__":
    app.run(debug=True)

