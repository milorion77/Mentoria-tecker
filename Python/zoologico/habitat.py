class Habitat:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.animales = []

    def agregarAnimal(self, animal):
        if len(self.animales) < self.capacidad:
            self.animales.append(animal)
            print(f"{animal.nombre} fue agregado al hábitat de {self.nombre}.")
        else:
            print(f"El hábitat de {self.nombre} está lleno. No se puede agregar a {animal.nombre}.")
