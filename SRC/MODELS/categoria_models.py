from connection import db
from passlib.context import CryptContext


class Categoria(db.Model):
    __tablename__ == "categoria"
 
    id = db.Column(db.Interger, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(120), nullable=False)
    
    produtos = db.relationship('Produto', back_populates='categoria', cascade='on delete')
