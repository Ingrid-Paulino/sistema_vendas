class Produto:
    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = int(quantidade)
        self.preco = int(preco)


    def retornar_produtos(self):
        return [self.id, self.nome, self.quantidade, self.preco]


    def retornar_produto(self):
        return self


    def __str__(self):
        return f"{self.id} {self.nome} {self.quantidade} {self.preco}"
