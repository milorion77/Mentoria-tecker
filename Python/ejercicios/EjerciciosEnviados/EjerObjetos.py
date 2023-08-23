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
