from crud_produto import *
from model_cliente import *
from tabulate import tabulate
from datetime import datetime


def criar_cliente(cliente_id):
    return Cliente(cliente_id, "cliente")

def arrecadacao_do_dia(clientes):
    tabela = [["Cliente", "Total"]]
    cliente_total = []

    for cliente in clientes:
        tabela.append(cliente.__gasto_total__(calculo_total_por_compra(cliente.compras)))
        cliente_total.append({"nome": f"{cliente.nome} {cliente.id}", "total": calculo_total_por_compra(cliente.compras)})

    mensagem(f"Data: {datetime.now()}")
    tabela = tabulate(tabela, headers="firstrow", tablefmt="fancy_grid")
    mensagem(tabela)

    total_vendas_estabelecimento = 0
    for total_vendas in cliente_total:
        total_vendas_estabelecimento = total_vendas_estabelecimento + total_vendas["total"]
    
    mensagem(f"Total de vendas: {total_vendas_estabelecimento}")

    return cliente_total