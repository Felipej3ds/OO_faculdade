class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.__notas = []

    def addNota(self,nota):
        self.__notas.append(nota)

    def removerNota(self):
        if len(self.__notas) == 0:
            return 0
        menor = min(self.__notas)
        return(self.__notas.remove(menor))

    def __iter__(self):
        self.__index = 0
        return self
    
    def __next__(self):
        if self.__index < len(self.__notas):
            nota = self.__notas[self.__index]
            self.__index += 1
            return nota
        else:
            raise StopIteration

	
a1 = Aluno("Glauco")
for item in a1:
        print(item)
a1.removerNota()
    