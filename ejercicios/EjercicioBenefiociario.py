personas = []
sumaEdadHombres = 0
sumaEdadMujeres = 0
hombresBeneficiados = 0
mujeresBeneficiados = 0

cantidadPersonas = int(input("Escriba la cantidad de personas que se van a inscribir: "))

for x in range(cantidadPersonas):
    ingresoEdad = int(input("Ingrese la edad de la persona: "))
    ingresoGenero = input("Ingrese el género de la persona (F/M): ").upper()
    ingresoEstrato = int(input("Ingrese el estrato de la persona: "))

    personas.append({'edad': ingresoEdad, 'genero': ingresoGenero, 'estrato': ingresoEstrato})

    if ingresoGenero == "M" and ingresoEdad <= 35 and ingresoEstrato in (1, 2):
        hombresBeneficiados += 1
        sumaEdadHombres += ingresoEdad
    elif ingresoGenero == "F" and ingresoEdad <= 30 and ingresoEstrato in (1, 2):
        mujeresBeneficiados += 1
        sumaEdadMujeres += ingresoEdad

if hombresBeneficiados > 0:
    promedioHombres = sumaEdadHombres / hombresBeneficiados
    print("La cantidad de hombres beneficiados es:", hombresBeneficiados)
    print("El promedio de edad de hombres beneficiados es:", promedioHombres)
else:
    print("No hay hombres beneficiados.")

if mujeresBeneficiados > 0:
    promedioMujeres = sumaEdadMujeres / mujeresBeneficiados
    print("La cantidad de mujeres beneficiadas es:", mujeresBeneficiados)
    print("El promedio de edad de mujeres beneficiadas es:", promedioMujeres)
else:
    print("No hay mujeres beneficiadas.")
