from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from models.map import MapModel

minha_requisicao = reqparse.RequestParser()

class User(Resource):

    @jwt_required()
    def get(self, id_r_map):
        map = MapModel.find_map_by_id(id_r_map)
        if map: 
            return map.json()
        return {'message':'User not found'}, 204

    @jwt_required()
    def delete(self, id_r_map):
        map = MapModel.find_map_by_id(id_r_map)
        if map:
            map.delete_map()
            return {'message' : 'Map deleted.'}
        return {'message' : 'Map not founded'}, 204

    @jwt_required()
    def post(self, id_r_map):
        dados = minha_requisicao.parse_args()

        if MapModel.find_map_by_ds_map(dados['ds_map_image']):
            return {'message':'Map {} already exists'.format(dados['ds_map_image'])}, 200
        id_r_map = MapModel.find_last_map()
        new_map = MapModel(id_r_map, **dados)
        
        try:
            print(new_map.json())
            new_map.save_map()
        except:
            return {'message':'An internal error ocurred.'}, 500

        return new_map.json(), 201
