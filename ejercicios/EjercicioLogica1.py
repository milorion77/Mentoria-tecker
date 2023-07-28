''' Para una campaña de salud se requiere determinar de un
grupo de N personas cuantos pueden beneficiarse.
Serán beneficiarios quienes siendo mujeres no pasen
de 30 años y quienes siendo hombres no superen los 35 años.
La campaña es solo para estratos 1 y 2. Se debe mostrar:

a. Cuantos hombres son beneficiados

b. Cuantas mujeres son beneficiadas

c. Mostrar el promedio de edad de hombres beneficiados

d. Mostrar el promedio de edad de mujeres beneficiadas

Indicar mediante un mensaje cuando no se es beneficiado. '''

class Beneficiario:
    def __init__(self, genero, edad, estrato):
        self.genero = genero
        self.edad = edad
        self.estrato = estrato
        self.es_beneficiado = self.es_beneficiado()

    def es_beneficiado(self):
        if self.genero == 'hombre' and self.edad <= 35 and self.estrato in (1, 2):
            return True
        elif self.genero == 'mujer' and self.edad <= 30 and self.estrato in (1, 2):
            return True
        else:
            return False

def prueba():
    personas = [
        {'genero': 'hombre', 'edad': 25, 'estrato': 2},
        {'genero': 'mujer', 'edad': 28, 'estrato': 1},
        {'genero': 'hombre', 'edad': 33, 'estrato': 2},
        {'genero': 'mujer', 'edad': 22, 'estrato': 2},

    ]

    # Variables para contar y acumular la edad de hombres y mujeres beneficiados
    hombres_beneficiados = 0
    mujeres_beneficiadas = 0
    edad_hombres_beneficiados = 0
    edad_mujeres_beneficiadas = 0

    # Variables para contar el total de hombres y mujeres
    total_hombres = 0
    total_mujeres = 0

    for persona in personas:
        genero = persona['genero']
        edad = persona['edad']
        estrato = persona['estrato']

        if Beneficiario(genero, edad, estrato).es_beneficiado:
            if genero == 'hombre':
                hombres_beneficiados += 1
                edad_hombres_beneficiados += edad
            elif genero == 'mujer':
                mujeres_beneficiadas += 1
                edad_mujeres_beneficiadas += edad

        # Contar el total de hombres y mujeres
        if genero == 'hombre':
            total_hombres += 1
        elif genero == 'mujer':
            total_mujeres += 1

    # Calcular el promedio de edad de hombres beneficiados y mujeres beneficiadas
    promedio_edad_hombres_beneficiados = edad_hombres_beneficiados / hombres_beneficiados if hombres_beneficiados > 0 else 0
    promedio_edad_mujeres_beneficiadas = edad_mujeres_beneficiadas / mujeres_beneficiadas if mujeres_beneficiadas > 0 else 0

    # Mostrar resultados
    print(f"Cantidad de hombres beneficiados: {hombres_beneficiados}")
    print(f"Cantidad de mujeres beneficiadas: {mujeres_beneficiadas}")
    print(f"Promedio de edad de hombres beneficiados: {promedio_edad_hombres_beneficiados}")
    print(f"Promedio de edad de mujeres beneficiadas: {promedio_edad_mujeres_beneficiadas}")

    # Mensaje para cuando no se es beneficiado
    if hombres_beneficiados == 0:
        print("No hay hombres beneficiados.")
    if mujeres_beneficiadas == 0:
        print("No hay mujeres beneficiadas.")


if __name__ == "__main__":
    prueba()
