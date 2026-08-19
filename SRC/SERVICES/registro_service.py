from SRC.MODELS.registro_models import Registro
from connection import db


def cadastrar_registro(registro):
    registro_db = Registro(
        nome=registro.get('nome'),
        uni_medida=registro.get('uni_medida'),
        qtd_estoque=registro.get('qtd_estoque')
    )
    db.session.add(registro_db)
    db.session.commit()
    return registro_db


def listar_registros():
    return Registro.query.all()


def listar_registro_por_id(id_registro):
    return Registro.query.get(id_registro)


def editar_registro(id_registro, novo_registro):
    registro = Registro.query.get(id_registro)
    if registro:
        registro.nome = novo_registro.get('nome', registro.nome)
        registro.uni_medida = novo_registro.get('uni_medida', registro.uni_medida)
        registro.qtd_estoque = novo_registro.get('qtd_estoque', registro.qtd_estoque)
        db.session.commit()
        return registro
    return None


def deletar_registro(id_registro):
    registro = Registro.query.get(id_registro)
    if registro:
        db.session.delete(registro)
        db.session.commit()
        return True
    return False


def salvar_registro(registro):
    return cadastrar_registro(registro)


def cancelar_registro(id_registro):
    return deletar_registro(id_registro)
