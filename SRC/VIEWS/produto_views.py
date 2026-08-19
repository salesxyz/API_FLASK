from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from SRC.SCHEMAS.produto_schemas import ProdutoSchema
from SRC.SERVICES import produto_serice as produto_service
from SRC import api

produto_schema = ProdutoSchema()
produto_schema_many = ProdutoSchema(many=True)


class ProdutoList(Resource):
    def get(self):
        produtos = produto_service.listar_produtos()
        if not produtos:
            return make_response(jsonify({"mensagem": "Nenhum produto encontrado"}), 404)
        return make_response(jsonify(produto_schema_many.dump(produtos)), 200)

    def post(self):
        try:
            produto_data = produto_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400
        try:
            resultado = produto_service.cadastrar_produto(produto_data)
            return produto_schema.dump(resultado), 201
        except Exception as e:
            return {'mensagem': str(e)}, 500


api.add_resource(ProdutoList, '/produtos')


class ProdutoResource(Resource):
    def get(self, id_produto):
        produto = produto_service.listar_produto_por_id(id_produto)
        if not produto:
            return make_response({"mensagem": "Produto não encontrado"}, 404)
        return produto_schema.dump(produto), 200

    def put(self, id_produto):
        try:
            produto_data = produto_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400
        atualizado = produto_service.editar_produto(id_produto, produto_data)
        if not atualizado:
            return {'mensagem': 'Produto não encontrado'}, 404
        return {'mensagem': 'Produto atualizado com sucesso!'}, 200

    def delete(self, id_produto):
        if produto_service.deletar_produto(id_produto):
            return {'mensagem': 'Produto deletado com sucesso!'}, 200
        return {'mensagem': 'Produto não encontrado'}, 404


api.add_resource(ProdutoResource, '/produtos/<int:id_produto>')

