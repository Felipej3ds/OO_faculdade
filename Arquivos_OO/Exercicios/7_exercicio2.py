class Pessoa:
    qtde = 0

    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf
        Pessoa.incrementaPessoa()

    @staticmethod
    def incrementaPessoa():
        Pessoa.qtde += 1

    def getCPF(self):
        return self.__cpf
    
p1 = Pessoa("Joao", 123)
p2 = Pessoa("Jose", 456)
print(Pessoa.qtde)  
print(p1.getCPF())
p2 = Pessoa("Jose", 456)
print(Pessoa.qtde)
print(p1.getCPF())
print(hasattr(p1, "cpf"))
print(p1._Pessoa__cpf)
