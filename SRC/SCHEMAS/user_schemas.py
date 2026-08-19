from marshmallow import fields

from SRC import ma
from SRC.MODELS.user_models import UsuarioModel


class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UsuarioModel
        load_instance = True
        fields = ('id', 'nome', 'email', 'senha')

    nome = fields.String(required=True)
    email = fields.Email(required=True)
    senha = fields.String(required=True)
