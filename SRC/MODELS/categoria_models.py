from connection import db


class Categoria(db.Model):
    __tablename__ = "categoria"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(120), nullable=False)

    produtos = db.relationship('Produto', back_populates='categoria', cascade='all, delete-orphan')
