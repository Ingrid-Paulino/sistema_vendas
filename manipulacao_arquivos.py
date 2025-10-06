import os.path
from model_produto import Produto

ARQ = 'produtos.csv'
DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(DIR, ARQ)

def ler_produtos():
    produtos = []
    try:
        with open(PATH, mode='r', encoding='utf-8') as arq:
            for linha in arq:
                campos = linha.split(',')
                id, nome, quantidade, preco = campos[0], campos[1], campos[2], campos[3]
                produto = Produto(id, nome, quantidade, preco)
                produtos.append(produto)
    except Exception as ex:
        print(ex)
    
    return produtos

def gravar_produtos(produtos):
    try:
        with open(ARQ, mode="w", encoding="UTF-8") as arq:
            for produto in produtos:
                arq.write(f"{produto.id}, {produto.nome}, {produto.quantidade}, {produto.preco} \n")
    except Exception as ex:
        print(ex)