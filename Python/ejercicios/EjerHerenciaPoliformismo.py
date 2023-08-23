class Vehiculo:
    def __init__(self, puertas, ruedas, color, tipo_combustible):
        self.puertas = puertas
        self.ruedas = ruedas
        self.color = color
        self.tipo_combustible = tipo_combustible

    def mostrar_informacion(self):
        """Muestra información sobre el vehículo."""
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
        """Indica si el auto es descapotable."""
        return self.descapotable

    def auto_sube(self):
        """Muestra si el auto está subiendo."""
        if self.subir:
            print("El Auto está subiendo.")

    def auto_baja(self):
        """Muestra si el auto está bajando."""
        if self.bajar:
            print("El Auto está bajando.")

class Camioneta(Vehiculo):
    def __init__(self, puertas, ruedas, color, tipo_combustible, carga_maxima):
        super().__init__(puertas, ruedas, color, tipo_combustible)
        self.carga_maxima = carga_maxima

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Esta camioneta puede transportar una carga máxima de {self.carga_maxima} kg.")

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

# Crear una lista de vehículos
vehiculos = [mi_auto, mi_camioneta, mi_ambulancia]

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        filtered_vehiculos = [v for v in vehiculos if v.ruedas == ruedas]
        print(f"Se han encontrado {len(filtered_vehiculos)} vehículos con {ruedas} ruedas:")
        for vehiculo in filtered_vehiculos:
            print(f"Clase: {type(vehiculo).__name__}")
            vehiculo.mostrar_informacion()
            print("\n")
    else:
        print("Catálogo de vehículos:")
        for vehiculo in vehiculos:
            print(f"Clase: {type(vehiculo).__name__}")
            vehiculo.mostrar_informacion()
            print("\n")

# Probar la función catalogar
catalogar(vehiculos)
catalogar(vehiculos, ruedas=2)
catalogar(vehiculos, ruedas=4)

#mi patroncito