from marshmallow import fields
from SRC import MA
from SRC.MODELS import ProdutoModel
from .categoria_schema import CategoriaSchema

class ProdutoSchema(ma.SQLAlchemyAutoSchema):

    nome = fields.String(
        required =True
        validate = validate.length(
            min = '3',
            error 'O nome deve ter no minimo 3 letras'
        )
    )
    
    uni_medida = fields.String(
        required = True
        validate = validate.OneOf(
            ['UN', 'KG', 'L', 'CX']
            error ='Unidade de medida invalida'
        )
    )

    qtd_estoque = fields.Interger(
        required = True
        validate = validate.Range(
            min= 0, 
            error = 'A quantidade não pode ser negativa!'
        )
    )

    vlr_unitario = fields.Decimal(
        required = True,
        places = 2,
        validate = validate.Range(
            min=0,
            error = 'O valor unitario deve ser maior ou igual a 0.'
        )
    )


    categoria = fields.Nested(
        CategoriaSchema,
        dump_only=True
    )
    class Meta:
        model = ProdutoModel
        load_instance = True
        include_fk=True

produto_schema = ProdutoSchema()


