from manipulacao_arquivos import *
from crud_produto import *
from menu import *
from crud_cliente import *

produtos = ler_produtos();


def abertura_do_caixa_main():
    compras_do_dia = []
    produtos_estoque = produtos

    while True:
        comecar_atendimento =  iniciar_atendimento() #da para verificar se esse cliente ja foi atendido hoje se sim atribuir as compras na mesma base
        if comecar_atendimento:
            cliente_id = len(compras_do_dia) + 1
            cliente = criar_cliente(cliente_id)

      
            opcao = escolher_opcao()
            while True:
                match (opcao):
                    case 1: 
                        listar_produtos(produtos_estoque)
                    case 2: 
                        compra = comprar_produto(produtos_estoque)
                        compra.item = len(cliente.compras) + 1
                        cliente.compras.append(compra)
                    case 0: 
                        compras_do_dia.append(cliente)
                        finalizar_atendimento(cliente)
                        break

                opcao = escolher_opcao()

        fechar_caixa = fechar_caixa_do_dia()
        if fechar_caixa:
            arrecadacao_do_dia(compras_do_dia)
            produtos_sem_estoque(produtos_estoque)
            gravar_produtos(produtos_estoque)
            break

abertura_do_caixa_main()
