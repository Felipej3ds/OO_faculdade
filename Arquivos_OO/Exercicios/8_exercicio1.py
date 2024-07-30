from abc import ABC, abstractmethod

class Endereco:
    def __init__(self, rua, numero, cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade

class Cliente(ABC):
    def __init__(self, codigo, nome, endereco):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self._saldo = 0  # Atributo protegido

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor > self._saldo:
            return "saldo insuficiente"
        else:
            self._saldo -= valor

    def getSaldo(self):
        return self._saldo

class PFisica(Cliente):
    def __init__(self, codigo, nome, endereco):
        super().__init__(codigo, nome, endereco)

class PJuridica(Cliente):
    def __init__(self, codigo, nome, endereco):
        super().__init__(codigo, nome, endereco)

e1 = Endereco("NSWT", 123,  "Brasilia")
e2 = Endereco("SQS", 77,  "Gama")
c1 = PFisica(123, "Glauco", e1)
c2 = PJuridica(222, "FGA", e2)
print(c1.endereco.cidade)
print(c2.endereco.cidade)