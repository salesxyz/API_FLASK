from connection import db
from passlib.context import CryptContext


class Registro(db.Model):
    __tablename__ == "usuarios"
 
    id = Column(Interger, primary_key=True, autoincrement=True)
    nome = Column(String(120), nullable=False)
    uni_medida = Column(String(100), nullable=False, unique=True)
    qtd_estoque = Column(String(255), unique=False)
