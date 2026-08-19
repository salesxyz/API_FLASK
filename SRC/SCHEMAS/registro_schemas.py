from marshmallow import fields, validate

from SRC import ma
from SRC.MODELS.registro_models import Registro


class RegistroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Registro
        load_instance = True
        fields = ('id', 'nome', 'uni_medida', 'qtd_estoque')

    nome = fields.String(required=True)

    uni_medida = fields.String(
        required=True,
        validate=validate.OneOf(
            ['UN', 'KG', 'L', 'CX'],
            error='Unidade de medida inválida'
        )
    )

    qtd_estoque = fields.Integer(
        required=True,
        validate=validate.Range(
            min=0,
            error='A quantidade não pode ser negativa!'
        )
    )


registro_schema = RegistroSchema()