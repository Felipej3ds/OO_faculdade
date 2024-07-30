class Aluno():
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def addNota(self, notas):
        self.notas.append(notas)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.notas):
            nota = self.notas[self._index]
            self._index += 1
            return nota
        else:
            raise StopIteration


a1 = Aluno("Glauco")
a1.addNota(5.3)
a1.addNota(2.1)
a1.addNota(1.3)
for item in a1:
    print(item)