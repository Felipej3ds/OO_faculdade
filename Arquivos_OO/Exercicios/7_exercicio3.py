from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def informacoes(self):
        pass

class Livro(Produto):

    def __init__(self, nome, qtdePaginas):
        super().__init__(nome)
        self.qtdePaginas = qtdePaginas
    def informacoes(self):
        return "este livro chama: " + self.nome + " que tem "+ str(self.qtdePaginas)+ " paginas"
    
class Televisao(Produto):
    def __init__(self, nome, polegadas):
        super().__init__(nome)
        self.polegadas = polegadas

    def informacoes(self):
        return "esta TV chama: " + self.nome + " que tem " + str(self.polegadas)+ " polegadas"
    
class CarrinhoCompras:
    def __init__(self):
        self.produtos = []

    def adicionar(self, Produtos):
        self.produtos.append(Produtos)
    
    def mostrarCarrinho(self):
            for item in self.produtos:
                  print(item.informacoes())

print(Produto.__abstractmethods__)
print(issubclass(Livro, Produto))
print(issubclass(Televisao, Produto))

