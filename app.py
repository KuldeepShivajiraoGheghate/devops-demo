"""
Simple Flask web application for the Jenkins GitHub Demo.

This is a beginner-friendly demo application with:
- A landing page
- A health check endpoint
- A greeting endpoint that accepts a name parameter
"""
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Simple HTML template for the landing page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Demo App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            text-align: center;
        }
        h1 {
            color: #667eea;
        }
        p {
            color: #555;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ greeting }}</h1>
        <p>Welcome to the DevOps Demo Application!</p>
        <p>Served by Flask on {{ server }}</p>
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    """Render the landing page."""
    return render_template_string(HTML_TEMPLATE,
                                  greeting="Hello, DevOps!",
                                  server="Flask")


@app.route("/greet/<name>")
def greet(name):
    """Return a personalized greeting for the given name."""
    cleaned_name = clean_input(name)
    return render_template_string(HTML_TEMPLATE,
                                  greeting=f"Hello, {cleaned_name}!",
                                  server="Flask")


@app.route("/health")
def health():
    """Health check endpoint for CI/CD verification."""
    return jsonify({"status": "healthy", "service": "devops-demo"}), 200


@app.route("/api/add/<int:a>/<int:b>")
def add(a, b):
    """Add two integers and return the result as JSON."""
    return jsonify({"result": a + b}), 200


def clean_input(value):
    """Sanitize user input to prevent HTML injection.

    Removes common HTML tags from the input string.
    This is a basic sanitizer for demonstration purposes.
    """
    safe_chars = []
    for char in value:
        if char.isalnum() or char in " -_. ":
            safe_chars.append(char)
    return "".join(safe_chars)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
