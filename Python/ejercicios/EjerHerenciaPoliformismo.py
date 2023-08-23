class Vehiculo:
    def __init__(self, puertas, ruedas, color, tipo_combustible):
        self.puertas = puertas
        self.ruedas = ruedas
        self.color = color
        self.tipo_combustible = tipo_combustible

    def mostrar_informacion(self):
        # Metodo para mostrar informacion del vehiculo
        print(f"Este vehículo tiene {self.puertas} puertas y {self.ruedas} ruedas.")
        print(f"Color: {self.color}")
        print(f"Tipo de combustible: {self.tipo_combustible}")


# Esta es la clase Auto que hereda de vehiculo
class Auto(Vehiculo):
    def __init__(
        self, puertas, ruedas, color, tipo_combustible, descapotable, subir, bajar
    ):
        super().__init__(puertas, ruedas, color, tipo_combustible)
        self.descapotable = descapotable
        self.subir = subir
        self.bajar = bajar

    # Metodo para saber si es decapotable
    def es_descapotable(self):
        """Indica si el auto es descapotable."""
        return self.descapotable

    # Metodo para ver si el auto sube
    def auto_sube(self):
        """Muestra si el auto está subiendo."""
        if self.subir:
            print("El Auto está subiendo.")

    # Metodo para ver si el auto baja
    def auto_baja(self):
        """Muestra si el auto está bajando."""
        if self.bajar:
            print("El Auto está bajando.")


# Esta es la clase camioneta que hereda de vehiculo
class Camioneta(Vehiculo):
    def __init__(self, puertas, ruedas, color, tipo_combustible, carga_maxima):
        super().__init__(puertas, ruedas, color, tipo_combustible)
        self.carga_maxima = carga_maxima

    # Metodo informacion heredado de vehiculo
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(
            f"Esta camioneta puede transportar una carga máxima de {self.carga_maxima} kg."
        )


# Esta es la clase Ambulacia que hereda de vehiculo
class Ambulancia(Vehiculo):
    def __init__(self, puertas, ruedas, color, tipo_combustible, equipo_medico):
        super().__init__(puertas, ruedas, color, tipo_combustible)
        self.equipo_medico = equipo_medico

    # Metodo informacion heredado de vehiculo
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Esta ambulancia está equipada con: {self.equipo_medico}")


class Motoneta(Vehiculo):
    def __init__(self, puertas, ruedas, color, tipo_combustible):
        super().__init__(puertas, ruedas, color, tipo_combustible)
    
    #Metodo mostrar informacion heredado de vehiculo
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Esta moto tiene: {self.ruedas} ruedas")


# Crear objetos de las clases hijas  o instanciando las clases hijas 
mi_auto = Auto(4, 4, "Verde", "Gasolina", True, True, False)
mi_camioneta = Camioneta(4, 4, "Rojo", "Gasolina", 1000)
mi_ambulancia = Ambulancia(4, 4, "Blanco", "Diésel", ["Desfibrilador", "Botiquín"])
mi_motoneta = Motoneta(0,2,"Azul","corriente")

# Crear una lista de vehículos para mostrar el poliformismo
vehiculos = [mi_auto, mi_motoneta, mi_camioneta, mi_ambulancia]  # Creo una lista llamada vehiculos para mostrar que las subclases se pueden agrupas asi no sean el mismo objeto



def catalogar(vehiculos, ruedas=0):
    if ruedas != 0:
        filtrar_vehiculos = [vehiculo for vehiculo in vehiculos if vehiculo.ruedas == ruedas]
         #lee como: 
         # "para cada vehiculo en la lista vehiculos, toma ese vehiculo y agrégalo a la nueva lista filtrar_vehiculos si cumple con la condición especificada".
        print(
            f"Se han encontrado {len(filtrar_vehiculos)} vehículos con {ruedas} ruedas:"
        )
        print("========================================================================================")
        for vehiculo in filtrar_vehiculos:
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

