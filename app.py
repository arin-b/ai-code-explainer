import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

#Load environment variables from .env file
load_dotenv()

# --- Flask App Setup ---
app = Flask(__name__) # Standar Flask app initialization

# configure the generative ai client
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-2.0-flash')
    print("AI model configured successfully.")
except Exception as e:
    print(f"Error configurinh AI model: {e}")
    model = None


def explain_code_snippet(code_snippet):
    """Sends the code snippet to the Gemini API and returns the explanation"""
    if not model:
        return "Error: AI model is not configured."

    #Improved prompt for better explanations:
    prompt = f"""Explain the following code snippet. Be clear, concise and focus on its purpose and key funcitonalities. Assume the reader is a computer science student.

    Code:
    {code_snippet}
    Explanation:"""

    try:
        response = model.generate_content(prompt)
        # Basic safety check (Gemini might sometimes refuse unsafe content)
        if response.parts:
            return response.text
        else:
            # Handle cases where response might be blocked or empty
            print("Warning: AI response might be empty or blocked")
            return "Could not get explanation (Response might be blocked or empty)"
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        # You might want to return a more user-friendly error message
        return f"Error generating explanation: {e}"


# --- Flask routes ---
@app.route('/')
def index():
    """Serves the main HTML page."""
    # Flask looks for templates in the 'templates' folder
    return render_template('index.html')


@app.route('/explain', methods=['POST'])
def handle_explain():
    """Receives code snippet from frontend, gets explanation, returns it."""
    if not request.is_json:
        return jsonify({"error:": "Request must be JSON"}), 400
    data = request.get_json()
    code = data.get('code')

    if not code:
        return jsonify({"error": "No code snippet provided"}), 400

    print(f"\nReceived code snippet:\n{code[:200]}...") # Log snippet start

    explanation = explain_code_snippet(code)

    print(f"Sending explanation:\n{explanation[:200]}...") # Log explanation start

    # Return the explanation in a JSON structure
    return jsonify({"explanation": explanation})


# --- Run the Flask app ---
if __name__ == "__main__":
    # Runs the development server. Debug=True auto-reloads when code changes.
    # Use host='0.0.0.0' to make it accessible on your network (optional)
    app.run(debug=True, port=5000, host='0.0.0.0') # You can choose another port if 5000 is busy


