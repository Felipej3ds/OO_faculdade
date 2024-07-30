from abc import ABC

class Agencia:
    qtdeClientes = 0

    def __init__(self, codigo):
        self.codigo = codigo
        self.cliente = []

    def addCliente(self, cliente):
        self.cliente.append(cliente)
        Agencia.qtdeClientes += 1

    def mostrarSaldo(self):
        saldo_total = 0
        for cliente in self.cliente:
            saldo_total += cliente.getSaldo()
        return saldo_total

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
    def __init__(self, codigo, nome, endereco, cpf):
        super().__init__(codigo, nome, endereco)
        self.cpf = cpf

class PJuridica(Cliente):
    def __init__(self, codigo, nome, endereco, cnpj):
        super().__init__(codigo, nome, endereco)
        self.cnpj = cnpj