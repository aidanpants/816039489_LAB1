from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    result = a + b 
    return jsonify({"operation": "addition", "result": result})

# Route for subtraction
@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    result = a - b 
    return jsonify({"operation": "subtraction", "result": result})

# Route for multiplication
@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    result = a * b 
    return jsonify({"operation": "multiplication", "result": result})

# Route for division
@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    if b == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400     # Handle division by zero
    result = a / b  
    return jsonify({"operation": "division", "result": result})

app.run(host='0.0.0.0', port=8080)