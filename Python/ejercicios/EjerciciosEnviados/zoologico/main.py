from animal import Animal
from leon import Leon
from cocodrilo import Cocodrilo
from cacatua import Cacatua
from habitat import Habitat

# Variables Globales
zoo_nombre = "Mi Zoológico"
zoo_direccion = "direccion inventadalandia"

# Crear instancias de animales
leon1 = Leon("León", "Macho", 5, 150, "Juanito")
cocodrilo1 = Cocodrilo("Cocodrilo", "Hembra", 7, 300, "Pedro")
cacatua1 = Cacatua("Cacatúa", "Hembra", 3, 0.5, "Luis")

# Crear instancias de hábitats
habitat_leones = Habitat("Hábitat de Leones", 5)
habitat_cocodrilos = Habitat("Hábitat de Cocodrilos", 3)
habitat_cacatuas = Habitat("Hábitat de Cacatúas", 2)

# Agregar animales a hábitats
habitat_leones.agregarAnimal(leon1)
habitat_cocodrilos.agregarAnimal(cocodrilo1)
habitat_cacatuas.agregarAnimal(cacatua1)

# Imprimir información del zoológico
print(f"Bienvenido a {zoo_nombre} ubicado en {zoo_direccion}.")
print("\nAnimales en el zoológico:")
leon1.imprimir()
leon1.rugir()
cocodrilo1.imprimir()
cocodrilo1.hacerSonido()
cacatua1.imprimir()
cacatua1.decirCucu()
