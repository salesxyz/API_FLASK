from SRC.MODELS.produto_models import Produto
from connection import db


def cadastrar_produto(produto):
    produto_db = Produto(
        nome=produto.get('nome'),
        uni_medida=produto.get('uni_medida'),
        qtd_estoque=produto.get('qtd_estoque'),
        vlr_unitario=produto.get('vlr_unitario'),
        fk_categoria_id=produto.get('fk_categoria_id')
    )
    db.session.add(produto_db)
    db.session.commit()
    return produto_db


def listar_produtos():
    return Produto.query.all()


def listar_produto_por_id(id_produto):
    return Produto.query.get(id_produto)


def editar_produto(id_produto, novo_produto):
    produto = Produto.query.get(id_produto)
    if produto:
        produto.nome = novo_produto.get('nome', produto.nome)
        produto.uni_medida = novo_produto.get('uni_medida', produto.uni_medida)
        produto.qtd_estoque = novo_produto.get('qtd_estoque', produto.qtd_estoque)
        produto.vlr_unitario = novo_produto.get('vlr_unitario', produto.vlr_unitario)
        if 'fk_categoria_id' in novo_produto:
            produto.fk_categoria_id = novo_produto['fk_categoria_id']
        db.session.commit()
        return produto
    return None


def deletar_produto(id_produto):
    produto = Produto.query.get(id_produto)
    if produto:
        db.session.delete(produto)
        db.session.commit()
        return True
    return False


def registrar_quantidade(id_produto, quantidade):
    produto = Produto.query.get(id_produto)
    if produto:
        produto.qtd_estoque += quantidade
        db.session.commit()
        return produto
    return None


def descricao(id_produto):
    produto = Produto.query.get(id_produto)
    if produto:
        return {
            'id': produto.id,
            'nome': produto.nome,
            'uni_medida': produto.uni_medida,
            'qtd_estoque': produto.qtd_estoque,
            'vlr_unitario': str(produto.vlr_unitario),
            'categoria': produto.categoria.nome if produto.categoria else None
        }
    return None
