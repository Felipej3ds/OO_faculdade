class ListaCompras:

    def __init__(self):
        self.produtos = []

    def addProduto(self, produto):
        if produto in self.produtos:
            print("produto já inserido")
        else:
            self.produtos.append(produto)
            print( "produto inserido" )
    
    def listarProdutos(self):
        if len(self.produtos) == 0:
            return "lista vazia"
        else:
            print(', '.join(self.produtos))

lista = ListaCompras()
print(lista.listarProdutos())
lista.addProduto("arroz")
lista.addProduto("arroz")
lista.addProduto("feijão")
lista.listarProdutos()
