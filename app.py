from flask import Flask
from flask_restx import Api, Resource
from ToDo.todo import Todo

app = Flask(__name__)
api = Api(app)

api.add_namespace(Todo, '/todos')

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)