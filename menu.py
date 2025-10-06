from util import *

def menu():
    print("MENU")
    print("[1]: Listar produtos")
    print("[2]: Comprar produtos")
    print("[0]: Finalizar atendimento \n")

OPCOES = (0, 1, 2)
def escolher_opcao():
    menu()
    while True:
        opcao =  entrar_inteiro("Digite uma opção: ")
        if opcao not in OPCOES:
            print("Error: onpção inválida")
        else: 
            break
    
    return opcao

def iniciar_atendimento():
    return sim_nao("Iniciar atendimento")
    
def fechar_caixa_do_dia():
    return sim_nao("Deseja fechar o caixa?")