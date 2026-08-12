from flask_resful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from src.schemas.produto_schema import (
    ProdutoSchema, ProdutoSchema
)
from src.services import user_service
from src import api 

