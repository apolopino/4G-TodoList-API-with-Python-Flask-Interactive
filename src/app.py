from flask import Flask, request, jsonify, json
app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
  return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
  body = request.data
  elemento = json.loads(body)
  todos.append(elemento)

  return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
  todos.pop(position)
  return jsonify(todos), 200



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)