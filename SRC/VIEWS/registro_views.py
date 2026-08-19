from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from SRC.SCHEMAS.registro_schemas import RegistroSchema
from SRC.SERVICES import registro_service
from SRC import api

registro_schema = RegistroSchema()
registro_schema_many = RegistroSchema(many=True)


class RegistroList(Resource):
    def get(self):
        registros = registro_service.listar_registros()
        if not registros:
            return make_response(jsonify({"mensagem": "Nenhum registro encontrado"}), 404)
        return make_response(jsonify(registro_schema_many.dump(registros)), 200)

    def post(self):
        try:
            registro_data = registro_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400
        try:
            resultado = registro_service.cadastrar_registro(registro_data)
            return registro_schema.dump(resultado), 201
        except Exception as e:
            return {'mensagem': str(e)}, 500


api.add_resource(RegistroList, '/registros')


class RegistroResource(Resource):
    def get(self, id_registro):
        registro = registro_service.listar_registro_por_id(id_registro)
        if not registro:
            return make_response({"mensagem": "Registro não encontrado"}, 404)
        return registro_schema.dump(registro), 200

    def put(self, id_registro):
        try:
            registro_data = registro_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400
        atualizado = registro_service.editar_registro(id_registro, registro_data)
        if not atualizado:
            return {'mensagem': 'Registro não encontrado'}, 404
        return {'mensagem': 'Registro atualizado com sucesso!'}, 200

    def delete(self, id_registro):
        if registro_service.deletar_registro(id_registro):
            return {'mensagem': 'Registro deletado com sucesso!'}, 200
        return {'mensagem': 'Registro não encontrado'}, 404


api.add_resource(RegistroResource, '/registros/<int:id_registro>')
