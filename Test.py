from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/users": {"origins": "http://localhost:63343"}})
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Привет от Flask!"})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify([
        {"id": 1, "name": "Алексей"},
        {"id": 2, "name": "Анна"}
    ])

@app.route('/user/<int:id>', methods=['GET'])
def get_user_by_id(id):  # Добавь параметр id
    users = [
        {"id": 1, "name": "Алексей"},
        {"id": 2, "name": "Анна"}
    ]
    user = next((u for u in users if u["id"] == id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

