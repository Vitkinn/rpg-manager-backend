from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token

from models.user import UserModel

minha_requisicao = reqparse.RequestParser()
minha_requisicao.add_argument('ds_password', type=str, required=True, help="ds_password is required")
minha_requisicao.add_argument('nm_user', type=str, required=True, help="nm_user is required")

class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = minha_requisicao.parse_args()
        user = UserModel.find_user_by_login(dados['nm_user'])
        if user and user.ds_password == dados['ds_password']:
            token_acesso = create_access_token(identity=user.id_user)
            return {'access_token': token_acesso}, 200
        return {'message': 'User or password is not correct.'}