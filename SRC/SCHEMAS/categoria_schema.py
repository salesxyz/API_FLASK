from marshmallow import fields

from SRC import ma
from SRC.MODELS.categoria_models import Categoria


class CategoriaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
        load_instance = True
        fields = ('id', 'descricao')

    descricao = fields.String(required=True)
