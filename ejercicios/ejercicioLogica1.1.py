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

def pruebaBeneficiario():
    personas = []
    continuar = True

    while continuar:
        genero = input("Ingrese el género (hombre'M'/mujer'F'): ")
        if genero != 'F' or 'M':
            genero = genero.upper()
        print(genero)

        edad = int(input("Ingrese la edad: "))
        estrato = int(input("Ingrese el estrato (1 o 2): "))

        personas.append({'genero': genero, 'edad': edad, 'estrato': estrato})

        respuesta = input("¿Desea ingresar otra persona? (s/n): ")
        if respuesta.lower() != 's':
            continuar = False

    print(personas)
    # VARIABLES PARA GUARDAR CONTEOS
    hombres_beneficiados = 0
    mujeres_beneficiadas = 0
    edad_hombres_beneficiados = 0
    edad_mujeres_beneficiadas = 0
    # VARIABLES PARA SUMAR TOTALES
    total_hombres = 0
    total_mujeres = 0

    for persona in personas:
        genero = persona['genero']
        edad = persona['edad']
        estrato = persona['estrato']

        if (genero == 'M' and edad <= 35 and estrato in (1, 2)) or (genero == 'mujer' and edad <= 30 and estrato in (1, 2)):
            if genero == 'M':
                hombres_beneficiados += 1
                edad_hombres_beneficiados += edad
            elif genero == 'F':
                mujeres_beneficiadas += 1
                edad_mujeres_beneficiadas += edad

        # Contar el total de hombres y mujeres
        if genero == 'M':
            total_hombres += 1
        elif genero == 'F':
            total_mujeres += 1

    # PROMEDIO
    promedio_edad_hombres_beneficiados = edad_hombres_beneficiados / hombres_beneficiados if hombres_beneficiados > 0 else 0
    promedio_edad_mujeres_beneficiadas = edad_mujeres_beneficiadas / mujeres_beneficiadas if mujeres_beneficiadas > 0 else 0

    print(f"Cantidad de hombres beneficiados: {hombres_beneficiados}")
    print(f"Cantidad de mujeres beneficiadas: {mujeres_beneficiadas}")
    print(f"Promedio de edad de hombres beneficiados: {promedio_edad_hombres_beneficiados}")
    print(f"Promedio de edad de mujeres beneficiadas: {promedio_edad_mujeres_beneficiadas}")

    # NO ES BENEFICIARIO
    if hombres_beneficiados == 0:
        print("No hay hombres beneficiados.")
    if mujeres_beneficiadas == 0:
        print("No hay mujeres beneficiadas.")


if __name__ == "__main__":
    pruebaBeneficiario()
