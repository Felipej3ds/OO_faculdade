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
    def __init__(self, codigo, nome, endereco):
        super().__init__(codigo, nome, endereco)


class PJuridica(Cliente):
    def __init__(self, codigo, nome, endereco   ):
        super().__init__(codigo, nome, endereco)

class Banco:
    def __init__(self, codigo):
        self.codigo = codigo
        self.agencia = {}

    def addAgencia(self, codigo_agencia):
        nova_agencia = Agencia(codigo_agencia)
        self.agencia[codigo_agencia] = nova_agencia

    def mostrarSaldo(self):
        saldo_total = 0
        for codigo_agencia, agencia in self.agencia.items():
            saldo_total += agencia.mostrarSaldo()
        return saldo_total
                         

e1 = Endereco("NSWT", 123,  "Brasilia")
e2 = Endereco("SQS", 77,  "Gama")
c1 = PFisica(123, "Glauco", e1)
c2 = PJuridica(222, "FGA", e2)
c1.depositar(100)
c2.depositar(80)
b = Banco(777)
b.addAgencia(101)
b.addAgencia(102)
b.agencia[101].addCliente(c1)
b.agencia[102].addCliente(c2)
print(b.mostrarSaldo())