from .user_models import UsuarioModel
from .categoria_models import Categoria
from .produto_models import Produto
from .registro_models import Registro

CategoriaModel = Categoria
ProdutoModel = Produto
RegistroModel = Registro

__all__ = [
    'UsuarioModel',
    'Categoria',
    'Produto',
    'Registro',
    'CategoriaModel',
    'ProdutoModel',
    'RegistroModel'
]