from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from SRC.SCHEMAS.produto_schemas import (
    ProdutoSchema, ProdutoSchema
)
from SRC.SERVICES import user_service
from SRC import api 

