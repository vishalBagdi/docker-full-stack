# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.json.get('name')
#     email = request.json.get('email')

#     return jsonify({
#         "message": "Data received",
#         "name": name,
#         "email": email
#     })

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.json.get('name')
    email = request.json.get('email')

    # Store data in data.txt
    with open('data.txt', 'a') as file:
        file.write(f"Name: {name}, Email: {email}\n")

    return jsonify({
        "message": "Data saved successfully",
        "name": name,
        "email": email
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)