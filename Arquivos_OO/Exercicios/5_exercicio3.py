from abc import ABC, abstractmethod

class Investimento(ABC):

    juros = 0.05
        
    @abstractmethod
    def jurosRendimento(self):
        pass

class Conta(Investimento):
    def __init__(self, numero, nome):
        self._saldo = 0
        self.numero = numero
        self.nome = nome

    def jurosRendimento(self):
        return self._saldo * Investimento.juros        
        
    def depositar(self, deposito):
        self._saldo +=  deposito
        self._saldo += self.jurosRendimento()

    @abstractmethod
    def sacar(self, valor):
        pass

    def getSaldo(self):
        return self._saldo
    
class Corrente(Conta):
    def __init__(self, numero, nome):
        super().__init__(numero, nome)

    def sacar(self, valor):
        valor_a_sacar = valor + (valor * 0.15)
        if valor_a_sacar > self._saldo:
            return("saldo insuficiente")
        else:
            self._saldo -= valor_a_sacar
            return True

class Poupanca(Conta):
    def __init__(self, numero, nome):
        super().__init__(numero, nome)

    def depositar(self, deposito):
        self._saldo += deposito

    def sacar(self, valor):
        valor_a_sacar = valor + (valor * 0.07)
        if valor_a_sacar > self._saldo:
            return"saldo insuficiente"
        else:
            self._saldo -= valor_a_sacar
            return True

    

c1 = Corrente(123,"Glauco")
c2 = Poupanca(123,"Glauco")
c1.depositar(100)
c2.depositar(80)
print(c2.getSaldo())
print(c1.getSaldo())