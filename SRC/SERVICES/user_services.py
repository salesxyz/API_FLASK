from SRC.MODELS.user_models import UsuarioModel
from connection import db


def cadastrar_usuario(usuario):
    usuario_db = UsuarioModel(
        nome=usuario.get('nome'),
        email=usuario.get('email'),
        senha=usuario.get('senha')
    )
    usuario_db.gen_senha(usuario.get('senha'))
    db.session.add(usuario_db)
    db.session.commit()
    return usuario_db


def listar_usuarios():
    return UsuarioModel.query.all()


def listar_usuario_por_id(id_usuario):
    return UsuarioModel.query.get(id_usuario)


def listar_usuario_por_email(email):
    return UsuarioModel.query.filter_by(email=email).first()


def deletar_usuario(id_usuario):
    usuario = UsuarioModel.query.get(id_usuario)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return True
    return False


def editar_usuario(id_usuario, novo_usuario):
    usuario = UsuarioModel.query.get(id_usuario)
    if usuario:
        usuario.nome = novo_usuario.get('nome', usuario.nome)
        usuario.email = novo_usuario.get('email', usuario.email)
        if novo_usuario.get('senha'):
            usuario.gen_senha(novo_usuario['senha'])
        db.session.commit()
        return usuario
    return None