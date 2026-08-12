from SRC.MODELS import CategoriaModel
from SRC import  ma
from marshmallow import fields

class CategoriaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CategoriaModel
        load_instance = True
        include_fk = True
    