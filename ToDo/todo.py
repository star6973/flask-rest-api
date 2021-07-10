from flask import request
from flask_restx import Resource, Api, Namespace

todos = {}
count = 1

todo_ns = Namespace(
    name="MyungHwa's TODO API",
    description="나만의 TODO 리스트를 위한 API"
)

@todo_ns.route('')
class TodoPost(Resource):
    def post(self):
        """ TODO 리스트 등록 """
        global count
        global todos

        idx = count
        count += 1
        todos[idx] = request.json.get('data')

        return {'todo_id': idx, 'data': todos[idx]}

@todo_ns.route('/<int:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        """ TODO 리스트 조회 """
        return {'todo_id': todo_id, 'data': todos[todo_id]}
    
    def put(self, todo_id):
        """ TODO 리스트 수정 """
        todos[todo_id] = request.json.get('data')
        return {'todo_id': todo_id, 'data': todos[todo_id]}
        
    def delete(self, todo_id):
        """ TODO 리스트 삭제 """
        del todos[todo_id]
        return {'delete': "success"}