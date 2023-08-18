## 
'''
Clases/ Objetos
Python es un lenguaje de programacion orientada a objetos
casi todo en py es un objeto, propiedades y metodos
una clase es como un contructor de objetos o un modelo para crear objetos 

creacion de clases
para la creacion de clases se usa la palabra class
 class nombreClase
'''
class ejemplo:
    x=14
## Objetos
Obj1=ejemplo()
print(Obj1.x)

## la funcion __init__()
## todas las clases tienen una funcion init siempre se ejecuta cuando se inicializa la clase 
#se usa para asignar valores a las propiedades a los objetos 

class persona:
    def __init__(self, nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
p1=persona("Juan", "Perez")
print(p1.apellido)

class animal:
    def __init__(this, patas, habitad, familia) :
        this.patas=patas
        this. habitad=habitad
        this.familia=familia

tigre=animal(4,"tierra", "felinos")
print(tigre.patas)
pajaro=animal(2,"aire", "Aves")
print(pajaro.patas)
print("================================================")

class Autor:
    def __init__(self, nombre, hojas, libro, dinero):
        self.nombre = nombre
        self.hojas = hojas
        self.libro = libro
        self.dinero = dinero
        self.tema = ""

    def escribir(self, tema):
        self.tema = tema
        print(f"{self.nombre} está escribiendo o escribió sobre {self.tema}")


class Editor:
    def __init__(self, marca, publicacion, precioxHoja):
        self.marca = marca
        self.publicacion = publicacion
        self.precioxHoja = precioxHoja

    def imprimir(self, texto):
        self.texto = texto
        print(f"{self.marca} está imprimiendo: {self.texto}")

    def cobrar(self, cobro):
        self.cobro = cobro
        print(f"{self.marca} está cobrando: ${self.cobro}")

#creo las instancias de clase que me piden en el diagrama
Rafa = Autor("Rafael Pombo", 32, "Mi pobre viejecita", 2500)
Norma = Editor("Norma", "1854", 1500)

Rafa.escribir("Erase una viejecita bien viejita que viajaba viejamente en su vejez")

Norma.imprimir(Rafa.libro)
Norma.cobrar(Rafa.hojas * Norma.precioxHoja)
