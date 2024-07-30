class Veiculo:

    def __init__(self):
        self.ocupacao = 0

    def embarcar(self, quantidade):
        if self.ocupacao + quantidade <= self.capacidade:
            self.ocupacao += quantidade
            return "embarque realizado"
        else:
            return "limite maximo atingido"

    def desembarcar(self, quantidade):
        if self.ocupacao == 0 and quantidade > self.ocupacao:
            return "desembarque nao realizado"
        else:
            self.ocupacao -= quantidade
            return "desembarque realizado"


class Carro(Veiculo):
    capacidade = 5


class Moto(Veiculo):
    capacidade = 2

c = Carro()
print(c.desembarcar(0))
print(c.embarcar(3))
print(c.desembarcar(5))

