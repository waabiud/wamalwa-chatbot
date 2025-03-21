from flask import Flask, render_template, request, jsonify
import aiml
import os

app = Flask(__name__)

# Initialize AIML Kernel
kernel = aiml.Kernel()

aiml_path = "aiml"  # Folder where AIML files are stored

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    for file in os.listdir(aiml_path):
        if file.endswith(".aiml"):
            kernel.learn(os.path.join(aiml_path, file))
    kernel.saveBrain("bot_brain.brn")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    message = request.form["messageText"].strip()
    bot_response = kernel.respond(message)
    return jsonify({"status": "OK", "answer": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

