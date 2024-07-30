class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getBonus(self, x):
        return self.salario*x
    
    def __eq__(self, funcionario):
        return self.nome == funcionario.nome
    
class Gerente(Funcionario):
    def bonifica(self, x):
        self.salario = self.salario+super().getBonus(x)

class Vendedor(Funcionario):
    def __init__( self, nome, salario, comissao):
        super().__init__(nome, salario)
        self.comissao = comissao

    def bonifica(self, x):
        self.salario = self.salario+(self.salario*x)+self.comissao


p1= Gerente("Joao", 1000)
p2 = Vendedor("José", 1000, 50)
p1.bonifica(10)
p2.bonifica(10)
print(p1.salario)
print(p2.salario)

p1= Gerente("Joao", 1000)
p2 = Vendedor("Joao", 1000, 50)
print(p1 == p2)
