class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.compras = []

    def __gasto_total__(self, total):
        return [f"{self.nome} {self.id}", total]
    
    def __str__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, compras={self.compras})"