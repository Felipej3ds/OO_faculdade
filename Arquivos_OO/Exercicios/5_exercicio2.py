class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def getSaldo(self):
        return self.saldo


class Investimento:
    juros = 0.05

    def jurosRendimento(self):
        self.saldo += self.saldo * Investimento.juros


class Corrente(Conta, Investimento):
    def depositar(self, valor):
        super().depositar(valor)
        self.jurosRendimento()


class Poupanca(Conta, Investimento):
    def depositar(self, valor):
        super().depositar(valor)
        self.jurosRendimento()

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")


# Teste
c1 = Corrente(123, "Glauco")
c2 = Poupanca(123, "Glauco")
c1.depositar(100)
c2.depositar(100)
c1.sacar(10)
c2.sacar(10)
print(c1.getSaldo())
print(c2.getSaldo())
print(c1.sacar(100))
print(c2.sacar(100))