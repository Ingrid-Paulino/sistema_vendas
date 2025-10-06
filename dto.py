class Compra:
    def __init__(self, item, nome, quantidade, preco, total):
        self.item = item
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.total = total


    def retornar_compras(self):
        return [self.item, self.nome, self.quantidade, self.preco, self.total]

