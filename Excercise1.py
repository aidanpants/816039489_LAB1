from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
        data = json.load(f)

@app.route('/count')
def get_counts():
    # Initialize counters dynamically
    count = {
        "Fish": 0,
        "Chicken": 0,
        "Vegetable": 0,
        "Computer Science (Special)": 0,
        "Computer Science (Major)": 0,
        "Information Technology (Special)": 0,
        "Information Technology (Major)": 0
    }

    for student in data:
        if student['pref'] in count:
            count[student['pref']] += 1

        if student['programme'] in count:
            count[student['programme']] += 1

    return jsonify(count)

@app.route('/students')
def get_students():
    result = []
    pref = request.args.get('pref')  # Get the meal preference parameter from URL
    programme = request.args.get('programme') 

    if pref and programme:
        # filter students by both meal preference and programme
        for student in data:
            if student['pref'] == pref and student['programme'] == programme:
                result.append(student)
        return jsonify(result)
    elif pref:
        # filter students by meal preference if only pref is provided
        for student in data:
            if student['pref'] == pref:
                result.append(student)
        return jsonify(result)
    elif programme:
        # filter students by programme if only programme is provided
        for student in data:
            if student['programme'] == programme:
                result.append(student)
        return jsonify(result)

app.run(host='0.0.0.0', port=8080)