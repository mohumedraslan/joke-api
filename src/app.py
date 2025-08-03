from flask import Flask, jsonify
from flask_cors import CORS
import random

# Create Flask application instance
app = Flask(__name__)

# Enable CORS for all routes and origins
CORS(app)

# Hardcoded list of 5 jokes
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What do you call a fake noodle? An impasta!",
    "Why did the math book look so sad? Because it had too many problems!"
]

@app.route('/')
def home():
    """
    Home endpoint with API information
    """
    return {
        "message": "Welcome to the Joke API!",
        "endpoints": {
            "/": "This home page",
            "/joke": "Get a random joke",
            "/health": "Health check"
        },
        "total_jokes": len(JOKES)
    }

@app.route('/joke')
def get_random_joke():
    """
    Returns a random joke from the hardcoded list
    """
    random_joke = random.choice(JOKES)
    return {
        "joke": random_joke,
        "status": "success",
        "total_jokes_available": len(JOKES)
    }

@app.route('/health')
def health_check():
    """
    Health check endpoint for monitoring
    """
    return {
        "status": "healthy",
        "message": "Joke API is running",
        "jokes_loaded": len(JOKES)
    }

if __name__ == '__main__':
    # Run the application on all interfaces (0.0.0.0) for Docker compatibility
    # Use port 5000 as the default Flask port
    app.run(host='0.0.0.0', port=5000, debug=True)

