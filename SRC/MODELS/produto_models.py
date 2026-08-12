from connection import db
from passlib.context import CryptContext


class Produto(db.Model):
    __tablename__ = "produto"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(120), nullable=False)
    uni_medida = db.Column(db.String(10), nullable=False)
    qtd_estoque = db.Column(db.Integer, nullable=False)
    vlr_unitario = db.Column(db.Numeric(10, 2), nullable=False)

    fk_categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    categoria = db.relationship("Categoria", back_populates='produtos')