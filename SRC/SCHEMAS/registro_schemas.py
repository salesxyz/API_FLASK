from SRC.MODELS import RegistroModel
from SRC import ma
from marshmallow import fields, validate

class RegistroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RegistroModel

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
        