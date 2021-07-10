from flask import Flask
from flask_restx import Api, Resource
from jinja2.utils import contextfunction
from ToDo.todo import todo_ns

app = Flask(__name__)
api = Api(
    app=app,
    verision='0.1',
    title="API Server",
    description="TODO API Server",
    terms_url='/',
    contact="battlesun99@gmail.com",
    license="MIT"
)

api.add_namespace(todo_ns, '/todos')

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)