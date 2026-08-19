from connection import db


class Registro(db.Model):
    __tablename__ = "registros"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(120), nullable=False)
    uni_medida = db.Column(db.String(100), nullable=False)
    qtd_estoque = db.Column(db.Integer, nullable=False)
