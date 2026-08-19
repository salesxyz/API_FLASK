from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from SRC.SCHEMAS.user_schemas import UsuarioSchema
from SRC.SERVICES import user_services as user_service
from SRC import api


usuario_schema = UsuarioSchema()
usuario_schema_many = UsuarioSchema(many=True)


class Usuariolist(Resource):
    def get(self):
        usuarios = user_service.listar_usuarios()
        if not usuarios:
            return make_response(jsonify({"mensagem": "Nenhum usuário encontrado"}), 404)
        return make_response(jsonify(usuario_schema_many.dump(usuarios)), 200)

    def post(self):
        try:
            usuario_data = usuario_schema.load(request.get_json())
        except ValidationError as e:
            return e.messages, 400
        if user_service.listar_usuario_por_email(usuario_data.get('email')):
            return {"mensagem": "Usuário já existe"}, 409
        try:
            resultado = user_service.cadastrar_usuario(usuario_data)
            return usuario_schema.dump(resultado), 201
        except Exception as e:
            return {'mensagem': str(e)}, 500


api.add_resource(Usuariolist, '/usuarios')


class UsuarioResource(Resource):
    def get(self, id_usuario):
        usuario = user_service.listar_usuario_por_id(id_usuario)
        if not usuario:
            return make_response({"mensagem": "Usuário não encontrado"}, 404)
        return usuario_schema.dump(usuario), 200

    def put(self, id_usuario):
        try:
            usuario_data = usuario_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400
        updated = user_service.editar_usuario(id_usuario, usuario_data)
        if not updated:
            return {'mensagem': "Usuário não encontrado"}, 404
        return {'mensagem': "Usuário atualizado com sucesso!"}, 200

    def delete(self, id_usuario):
        if user_service.deletar_usuario(id_usuario):
            return {'mensagem': "Usuário deletado com sucesso!"}, 200
        return {'mensagem': "Usuário não encontrado"}, 404


api.add_resource(UsuarioResource, '/usuarios/<int:id_usuario>')
