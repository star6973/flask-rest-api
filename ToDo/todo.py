from flask import request
from flask_restx import Resource, Api, Namespace, fields

todos = {}
count = 1

todo_ns = Namespace(
    name="MyungHwa's TODO API",
    description="나만의 TODO 리스트를 위한 API"
)

# 모델 객체 생성
todo_fields = todo_ns.model("TODO Fields", {
    'data': fields.String(description="a Todo", required=True, example="what to do")
})

todo_fields_with_id = todo_ns.inherit("TODO with ID", todo_fields, {
    'todo_id': fields.Integer(description="a TODO ID")
})

@todo_ns.route('')
class TodoPost(Resource):
    @todo_ns.expect(todo_fields)
    @todo_ns.response(code=201, description="Success", model=todo_fields_with_id)
    def post(self):
        """ TODO 리스트 등록 """
        global count
        global todos

        idx = count
        count += 1
        todos[idx] = request.json.get('data')

        return {'todo_id': idx, 'data': todos[idx]}

@todo_ns.route('/<int:todo_id>')
@todo_ns.doc(params={'todo_id': "ID"})
class TodoSimple(Resource):
    def get(self, todo_id):
        """ TODO 리스트 조회 """
        return {'todo_id': todo_id, 'data': todos[todo_id]}
    
    def put(self, todo_id):
        """ TODO 리스트 수정 """
        todos[todo_id] = request.json.get('data')
        return {'todo_id': todo_id, 'data': todos[todo_id]}
    
    @todo_ns.doc(response={202: "Success"})
    @todo_ns.doc(response={500: "Failed"})
    def delete(self, todo_id):
        """ TODO 리스트 삭제 """
        del todos[todo_id]
        return {'delete': "success"}, 202