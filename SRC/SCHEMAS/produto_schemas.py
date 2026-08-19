from marshmallow import fields, validate

from SRC import ma
from SRC.MODELS.produto_models import Produto
from .categoria_schema import CategoriaSchema


class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Produto
        load_instance = True
        fields = ('id', 'nome', 'uni_medida', 'qtd_estoque', 'vlr_unitario', 'fk_categoria_id', 'categoria')

    nome = fields.String(
        required=True,
        validate=validate.Length(
            min=3,
            error='O nome deve ter no minimo 3 letras'
        )
    )

    uni_medida = fields.String(
        required=True,
        validate=validate.OneOf(
            ['UN', 'KG', 'L', 'CX'],
            error='Unidade de medida invalida'
        )
    )

    qtd_estoque = fields.Integer(
        required=True,
        validate=validate.Range(
            min=0,
            error='A quantidade não pode ser negativa!'
        )
    )

    vlr_unitario = fields.Decimal(
        required=True,
        places=2,
        validate=validate.Range(
            min=0,
            error='O valor unitario deve ser maior ou igual a 0.'
        )
    )

    fk_categoria_id = fields.Integer(required=True)

    categoria = fields.Nested(
        CategoriaSchema,
        dump_only=True
    )


produto_schema = ProdutoSchema()


