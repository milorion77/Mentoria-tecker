class Vehiculo:
    def __init__(self, puertas, ruedas, color, tipo_combustible):
        self.puertas = puertas
        self.ruedas = ruedas
        self.color = color
        self.tipo_combustible = tipo_combustible

    def mostrar_informacion(self):
        print(f"Este vehículo tiene {self.puertas} puertas y {self.ruedas} ruedas.")
        print(f"Color: {self.color}")
        print(f"Tipo de combustible: {self.tipo_combustible}")

class Auto(Vehiculo):
    def __init__(self, puertas, ruedas, color, tipo_combustible, descapotable, subir, bajar):
        super().__init__(puertas, ruedas, color, tipo_combustible)
        self.descapotable = descapotable
        self.subir = subir
        self.bajar = bajar

    def es_descapotable(self):
        return self.descapotable

    def auto_sube(self):
        if self.subir:
            print("El Auto está subiendo.")

    def auto_baja(self):
        if self.bajar:
            print("El Auto está bajando.")

    def mostrar_informacion(self):
        super().mostrar_informacion()
        descapotable = "descapotable" if self.es_descapotable() else "no descapotable"
        print(f"Este auto es {descapotable}.")
                

#clase hija Camioneta que hereda de Vehiculo
class Camioneta(Vehiculo):
    def __init__(self, puertas, ruedas, color, tipo_combustible, carga_maxima):
        super().__init__(puertas, ruedas, color, tipo_combustible)
        self.carga_maxima = carga_maxima

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Esta camioneta puede transportar una carga máxima de {self.carga_maxima} kg.")

#clase hija Ambulancia que hereda de Vehiculo
class Ambulancia(Vehiculo):
    def __init__(self, puertas, ruedas, color, tipo_combustible, equipo_medico):
        super().__init__(puertas, ruedas, color, tipo_combustible)
        self.equipo_medico = equipo_medico

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Esta ambulancia está equipada con: {self.equipo_medico}")

# Crear objetos de las clases hijas
mi_auto = Auto(4, 4, "Verde", "Gasolina", True, True, False)
mi_camioneta = Camioneta(4, 4, "Rojo", "Gasolina", 1000)
mi_ambulancia = Ambulancia(4, 4, "Blanco", "Diésel", ["Desfibrilador", "Botiquín"])

# Llamar al método para mostrar información de los objetos
mi_auto.mostrar_informacion()
mi_camioneta.mostrar_informacion()
mi_ambulancia.mostrar_informacion()
