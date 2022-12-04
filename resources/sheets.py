from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token

from models.sheet import SheetModel

minha_requisicao = reqparse.RequestParser()

class Sheet(Resource):

    @jwt_required()
    def get(self, id_sheet):
        sheet = SheetModel.find_sheet_by_name(id_sheet)
        if sheet: 
            return sheet.json()
        return {'message':'Sheet not found'}, 204

    @jwt_required()
    def delete(self, id_sheet):
        sheet = SheetModel.find_sheet_by_name(id_sheet)
        if sheet:
            sheet.delete_sheet()
            return {'message' : 'Sheet deleted.'}
        return {'message' : 'Sheet not founded'}, 204

    @jwt_required()
    def post(self, id_sheet):
        dados = minha_requisicao.parse_args()

        if SheetModel.find_sheet_by_name(dados['nm_character']):
            return {'message':'Character {} already exists'.format(dados['nm_character'])}, 200
        id_sheet = SheetModel.find_last_sheet()
        new_sheet = SheetModel(id_sheet, **dados)
        
        try:
            print(new_sheet.json())
            new_sheet.save_sheet()
        except:
            return {'message':'An internal error ocurred.'}, 500

        return SheetModel.json(), 201
