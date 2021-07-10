from flask import Flask, request
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version="1.0", title="상품 관리 API", description="상품 등록, 수정, 삭제, 조회 API")
ns = api.namespace("goods", description="상품 등록, 수정, 삭제, 조회")

# refine data model
model_goods = api.model('row_goods', {
    'id': fields.Integer(readOnly=True, required=True, description="상품번호"),
    'goods_name': fields.String(required=True, description="상품명")
})

class GoodsDAO(object):
    ''' 상품 정보 데이터 접근 객체 '''
    def __init__(self):
        self.counter = 0
        self.rows = []

    ''' 상품 정보 조회 '''
    def get(self, id):
        for row in self.rows:
            if row['id'] == id:
                return row
        api.abort(404, "{} doesn't exist".format(id))

    ''' 상품 정보 등록 '''
    def create(self, data):
        row = data
        row['id'] = self.counter = self.counter + 1
        self.rows.append(row)
        return row

    ''' 상품 정보 수정 '''
    def update(self, id, data):
        row = self.get(id)
        row.update(data)
        return row

    ''' 상품 정보 삭제 '''
    def delete(self, id):
        row = self.get(id)
        self.rows.remove(row)

DAO = GoodsDAO()
DAO.create({'goods_name': '삼성 갤럭시북 Pro'})
DAO.create({'goods_name': 'LG Gram'})

@ns.route('/')
class GoodsListManager(Resource):
    @ns.marshal_list_with(model_goods)
    def get(self):
        return DAO.rows

    @ns.expect(model_goods)
    @ns.marshal_with(model_goods, code=201)
    def post(self):
        return DAO.create(api.payload), 201 

@ns.route('/<int:id>')
@ns.response(404, 'id를 찾을 수가 없습니다')
@ns.param('id', '상품 번호를 입력하세요')
class GoodsRunManager(Resource):
    @ns.marshal_with(model_goods)
    def get(self, id):
        return DAO.get(id)

    def delete(self, id):
        DAO.delete(id)
        return '', 200

    @ns.expect(model_goods)
    @ns.marshal_with(model_goods)
    def put(self, id):
        return DAO.update(id, api.payload)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)