class Pares:
    def __init__(self, valor):
        self.valor = valor
        self.atual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual > self.valor:
            raise StopIteration
        else:
            par = self.atual
            self.atual += 2
            return par