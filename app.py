from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

def get_chatbot_response(user_input):
    """
    Returns a predefined response based on keywords in the user's input.
    """
    # Convert user input to lowercase to make matching easier
    user_input = user_input.lower()

    # --- Define Rules ---
    if "hello" in user_input or "hi" in user_input:
        return "Hello there! This is your full-stack chatbot."
    
    elif "how are you" in user_input:
        return "I'm a web app, running perfectly on a Flask backend!"
    
    elif "what is your name" in user_input or "who are you" in user_input:
        return "I'm a chatbot built with a separate frontend and backend."
    
    elif "help" in user_input:
        return "I can understand 'hello', 'how are you', and 'what is your name'. Type 'bye' to exit."
        
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day."
    
    # --- Default Response ---
    else:
        return "I'm sorry, I don't understand that. My rules are still simple."

# --- Define Routes ---

@app.route("/")
def home():
    """
    This route serves the main HTML page (our frontend).
    """
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """
    This route handles the chat messages.
    It receives a message from the frontend and returns the bot's response.
    """
    # Get the user's message from the JSON data sent by the frontend
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"response": "Error: No message received."})

    # Get the bot's response
    bot_response = get_chatbot_response(user_message)
    
    # Return the response as JSON
    return jsonify({"response": bot_response})

# --- Run the App ---

if __name__ == "__main__":
    app.run(debug=True)








