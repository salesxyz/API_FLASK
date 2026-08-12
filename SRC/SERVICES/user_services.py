from SRC.MODELS.user_models import UsuarioModel
from connection import db

def cadastrar_Usuario(usuario):
    usuario_db = UsuarioModel(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario_db.gen_senha(usuario.senha)
    db.session.add(usuario_db)
    db.session.commit()
    return usuario_db

#listar todos os usuarios
def listar_usuario():
    return UsuarioModel.query.all()


#listar usuario por id
def listar_usuario_id():
    usuario_encontrado = UsuarioModel.query.get(id)
    return usuario_encontrado


#listar usuario por email
def listar_usuario_email(email):
    return UsuarioModel.query.filter_by(UsuarioModel.email == email).first()

def deletar_usuario(id):
    usuario = UsuarioModel.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return True
    return False

def editar_usuario(id, novo_usuario):
    usuario = UsuarioModel.query.get(id)
    if usuario:
        usuario.nome = novo_usuario['nome']
        usuario.email = novo_usuario['email']
        if novo_usuario(novo_usuario['senha']):
            usuario.senha = novo_usuario['senha']

        db.session.commit()
        return usuario
    
    return None