class Animal:
    def __init__(self, nombre, genero, edad, peso, esCarnivoro, esHerbivoro, cuidador):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.peso = peso
        self.esCarnivoro = esCarnivoro
        self.esHerbivoro = esHerbivoro
        self.cuidador = cuidador

    def imprimir(self):
        print(f"El nombre del animal es: {self.nombre}. El nombre del cuidador es: {self.cuidador}")
        print(f"Genero: {self.genero}, Edad: {self.edad}, Peso: {self.peso}kg, Carnivoro: {self.esCarnivoro}, Herbivoro: {self.esHerbivoro}")

    def darDeComer(self):
        if self.esCarnivoro and self.esHerbivoro:
            print(f"{self.nombre} come de todo.")
        elif self.esCarnivoro:
            print(f"Cuidador {self.cuidador} da de comer solo carne a {self.nombre}.")
        elif self.esHerbivoro:
            print(f"Cuidador {self.cuidador} da de comer solo frutas y vegetales a {self.nombre}.")
