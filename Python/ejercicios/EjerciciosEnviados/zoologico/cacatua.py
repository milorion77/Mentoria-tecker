from animal import Animal

class Cacatua(Animal):
    def __init__(self, nombre, genero, edad, peso, cuidador):
        super().__init__(nombre, genero, edad, peso, False, True, cuidador)

    def decirCucu(self):
        print(f"{self.nombre} dice 'cucú, cucú' como una cacatúa.")
