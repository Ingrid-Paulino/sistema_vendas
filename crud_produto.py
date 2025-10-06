from tabulate import tabulate
from model_produto import Produto
from util import *
from dto import *
from datetime import datetime


def listar_produtos(prods: list[Produto]) -> list[Produto]:
    tabela = [["id", "nome", "quantidade", "preco"]]
    produtos = []
    for produto in prods:
        produtos.append(produto.retornar_produto())
        tabela.append(produto.retornar_produtos())
    
    print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"), "\n\n")
    return produtos


def buscar_produto(produtos, produto_id):
    produto = None
    for prod in produtos:
        if int(prod.id) == produto_id and prod.quantidade > 0:
            produto = prod
            return produto
    
    return produto

def comprar_produto(produtos):
    tabela = [["id", "nome", "quantidade", "preco"]]
    produto = None

    while True:
        produto_id = entrar_inteiro("Digite o id do produto que deseja:")
        produto = buscar_produto(produtos, produto_id)
        if  produto != None:
            break

        mensagem("Erro: produto não cadastrado ou sem estoque")

    tabela.append(produto.retornar_produtos())
    print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"), "\n\n")
    
    while True:
        qtd_produto_cliente = entrar_inteiro("Digite a quantidade de produtos que deseja:")
        if qtd_produto_cliente > produto.quantidade:
            mensagem(f"Erro: temos {produto.quantidade} itens no estoque. Escolha uma quantidade igual ou inferior")
        elif qtd_produto_cliente == 0:
            mensagem("Erro: quantidade deve ser maior que zero”")
        else:
            baixa_de_produto_no_estoque(produtos, qtd_produto_cliente, int(produto.id)) #melhorar esses nomes de variaveis
            break

    return Compra("", produto.nome, qtd_produto_cliente, produto.preco, produto.preco * qtd_produto_cliente)


"""valor do estoque esta sendo alterado por referencia na memoria"""
def baixa_de_produto_no_estoque(produtos, qtd_produto_comprado, id):
    mensagem("Baixa no estoque:")
    produto = buscar_produto(produtos, id)
    produtos[int(produto.id) - 1].quantidade = produto.quantidade - qtd_produto_comprado

def finalizar_atendimento(cliente):
    mensagem("Finalizar atendimento")
    nota_fiscal(cliente)

def nota_fiscal(cliente):
    tabela = [["Item", "Produto", "Quant.", "preço", "Total"]]
    cesta_compras = cliente.compras

    for produto in cesta_compras:
        tabela.append(produto.retornar_compras()) 
    
    mensagem(f"{cliente.nome} {cliente.id}")
    mensagem(f"Data: {datetime.now()}")
    mensagem(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"))
    mensagem(f"Itens: {len(cliente.compras)}")
    mensagem(f"Total: {calculo_total_por_compra(cliente.compras)}")

def calculo_total_por_compra(compras):
    total = 0
    for compra in compras:
        total = total + (compra.preco * compra.quantidade)
    
    return total

def produtos_sem_estoque(produtos):
    mensagem("Produtos sem estoque:")
    tabela = [["Produto"]]
    for produto in produtos:
        if produto.quantidade == 0:
            tabela.append([f"{produto.nome}"])
    tabela = tabulate(tabela, headers="firstrow", tablefmt="fancy_grid")
    mensagem(tabela)