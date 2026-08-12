from flask_resful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from src.schemas.user_schema import (
    UsuarioSchema, UsuarioSchema
)
from src.services import user_service
from src import api 


class Usuariolist(Resource):
    def get(self):
        usuarios = user_Service.listar_usuarios()

        if not usuarios:
                rerturn make_response(jsonify({"mensagem": "Nenhum usuário encontrado"}), 404)
        
        return make_response(jsonify(usuario_schema.dump(usuarios)), 200)
    
    def post(self):
        try:
            usuario = usuario_schema.load(request.get_json())
        except ValidationError as e:
            return err.messages, 400
        if user_service.listar_usuario_por_email(usuario.email):
            return {mensagem: "Usuário já existe"}, 409
        try:
            resultado = user_service.cadastrar_usuario(usuario)
            return usuario_schema.dump(resultado), 201

        except Exception as e:
            return {
                'messagem':str(e)
            }

        
api.add_resource(Usuariolist, '/usuarios')


class UsuarioResource(Resource):
    def get(self, id_usuario):
        usuario = user_service.listar_usuario_por_id(id_usuario)
        if not usuario:
            return make_response(
                {mensagem: "Usuário não encontrado"}, 404
            )
       return usuario_schema.dump(usuario), 200


    def put(self, id_usuario):
        try:
            usuario = usuario_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400
            user_services.editar_usuario(id_usuario, {
                'nome': usuario_nome.nome
                'email': usuario_email.email
                'senha': usuario_senha.senha
            })
        if not usuario:
            return {
                'mensagem': "Usuário não encontrado"
            }, 404
         return {
            'mensagem': "Usuário atualizado com sucesso!"
        }, 200


    def delete(self, id_usuario):
        if user_service.deletar_usuario(id_usuario):
            return {
                'mensagem': "Usuário deletado com sucesso!"
            },200
        return {
            'mensagem': "Usuário não encontrado"
        }, 404

api.add_resource(UsuarioResource, '/usuarios/<int:id>')
