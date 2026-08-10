from SRC.MODELS import RegistroModel
from SRC import  MA
from marshmallow import fields

class RegistroModel(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CategoriaModel
    
      
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
        