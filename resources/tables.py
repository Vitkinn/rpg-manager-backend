from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from models.table import TableModel

minha_requisicao = reqparse.RequestParser()
minha_requisicao.add_argument('nm_table', type=str, required=True, help="nm_user is required")
minha_requisicao.add_argument('ds_table', type=str, required=False)

class Table(Resource):

    @jwt_required()
    def get(self, id_table):
        table = TableModel.find_table_by_id(id_table)
        if table: 
            return table.json()
        return {'message':'Table not found'}, 204

    @jwt_required()
    def delete(self, id_table):
        table = TableModel.find_table_by_id(id_table)
        if table:
            table.delete_table()
            return {'message' : 'Table deleted.'}
        return {'message' : 'Table not founded'}, 204

    def post(self, id_table):
        dados = minha_requisicao.parse_args()

        if TableModel.find_user_by_login(dados['nm_table']):
            return {'message':'Table {} already exists'.format(dados['nm_table'])}, 200
        id_table = TableModel.find_last_user()
        new_table = TableModel(id_table, **dados)
        
        try:
            print(new_table.json())
            new_table.save_user()
        except:
            return {'message':'An internal error ocurred.'}, 500

        return new_table.json(), 201

#class UserLogin(Resource):

 #   @classmethod
  #  def post(cls):
   #     dados = minha_requisicao.parse_args()
    #    user = UserModel.find_user_by_login(dados['nm_table'])

     #   if user and user.ds_password == dados['ds_password']:
      #      token_acesso = create_access_token(identity=user.id_user)
       #     return {'access_token': token_acesso}, 200
        #return {'message': 'User or password is not correct.'}
