from animal import Animal

class Leon(Animal):
    def __init__(self, nombre, genero, edad, peso, cuidador):
        super().__init__(nombre, genero, edad, peso, True, False, cuidador)

    def rugir(self):
        print(f"{self.nombre} ruge como un león.")
