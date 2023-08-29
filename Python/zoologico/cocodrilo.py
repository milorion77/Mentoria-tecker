from animal import Animal

class Cocodrilo(Animal):
    def __init__(self, nombre, genero, edad, peso, cuidador):
        super().__init__(nombre, genero, edad, peso, True, False, cuidador)

    def hacerSonido(self):
        print(f"{self.nombre} hace sonidos de cocodrilo.")
