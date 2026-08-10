    from connection import db
    from passlib.context import CryptContext


    class UsuarioModel(db.Model):
        __tablename__ == "usuarios"
    
        id = Column(Interger, primary_key=True, autoincrement=True)
        nome = Column(String(100), nullable=False)
        email = Column(String(100), nullable=False, unique=True)
        senha = Column(String(255), nullable=False)


        pwd_context = CryptContext(schemes=['argon2'], deprecated='auto')


        def gen_senha(self, senha):
            self.senha = self.pwd_context.hash(senha)


        def verifica_senha(self, senha):
            return self.pwd_context.verify(senha, self.senha)
        

