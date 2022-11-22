from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import jwt_required

minha_requisicao = reqparse.RequestParser()
minha_requisicao.add_argument('nm_user', type=str, required=True, help="Login is required")
minha_requisicao.add_argument('ds_email', type=str, required=True, help="Email is required")
minha_requisicao.add_argument('ds_password', type=str, required=True, help="Password is required")
minha_requisicao.add_argument('ds_name', type=str, required=True, help="Name is required")
minha_requisicao.add_argument('nr_contact', type=str, required=True, help="Contact is required")
#minha_requisicao.add_argument('ds_avatar', type=str, required=False, help="Avatar is required")

class User(Resource):

    ##@jwt_required()
    def get(self, id_user):
        user = UserModel.find_user_by_id(id_user)
        if user: 
            return user.json()
        return {'message':'user not found'}, 200 # or 204

    @jwt_required()
    def delete(self, id_user):
        user = UserModel.find_user_by_id(id_user)
        if user:
            user.delete_user()
            return {'message' : 'user deleted.'}
        return {'message' : 'user not founded'}, 204

    def post(self, id_user):
        dados = minha_requisicao.parse_args()
        if UserModel.find_user_by_login(dados['nm_user']):
            return {'message':'Login {} already exists'.format(dados['nm_user'])}, 200

        id_user = UserModel.find_last_user()
        new_user = UserModel(id_user, **dados)
        
        try:
            print(new_user.json())
            new_user.save_user()
        except:
            return {'message':'An internal error ocurred.'}, 500

        return new_user.json(), 201

class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = minha_requisicao.parse_args()
        user = UserModel.find_user_by_login(dados['nm_user'])

        if user and user.ds_password == dados['ds_password']:
            token_acesso = create_access_token(identity=user.id_user)
            return {'access_token': token_acesso}, 200
        return {'message': 'User or password is not correct.'}
