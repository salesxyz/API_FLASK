from SRC.MODELS.produto_models import ProdutoModel
from connection import db

#cadastrar o produto pelo ID
def cadastrar_Produto(id):
  registro_db = ProdutoModel(id=id)
  db.session.add(registro_db)
  db.session.commit()

def registrar_quantidade():
    ...
def descricao():
  ...