from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from SRC.MODELS import user_models
from marshmallow import fields

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = user_models.UsuarioModel
        load_instance = True
        fields = ('id', 'nome', 'email', 'senha')


    nome = fields.String(required=True)
    email = fields.Email(required=True)
    senha = fields.String(required=True)
     