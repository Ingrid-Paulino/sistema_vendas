def entrar_inteiro(msg):
    try:
        num = int(input(msg))
        return num
    except Exception as ex:
        print(f"Erro: valor inválido. {ex}")

def sim_nao(msg):
    print(msg)
    resposta = input("Digite [y] ou [n]:").upper()
    while resposta != "Y" and resposta != "N":
        resposta = input("Digite [y] ou [n]:").upper()

    if resposta == "N":
        return False
    return True 

def mensagem(msg):
    print(msg) 