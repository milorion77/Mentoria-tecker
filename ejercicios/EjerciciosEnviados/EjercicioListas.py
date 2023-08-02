## tipos de datos listas 
## los elementos pueden ser de cualquier tipo 
string=["txt","hola","hidih","uidxiud"]
interger=[78,45,23,11,10,98]
flotantes=[78.0,45.1,12,78.0,45.23,78.0]
booleanos=[True,False,False,True,True,False,True,True]
mixta=["pepito","perez",25,"veeronfrng",12552241,True]
print(string)
print(interger)
print(flotantes)
print(booleanos)
print(mixta)
## type 
print(type(mixta))
## acceso
print()
print(string[2])
print(string[1:3])
print(string[-1])
## comprobar si un articulo existe en una lista 
## para determinar si un elemento especifico existe en una lista usamos la palabra clave in
print("pepito" not in mixta)

####SOLUCIONES

# 5. recorrer en for interger y validar si el 98,11 existe y la cantidad
existe = [98,11]
for enteros in existe:
    if enteros in interger:
        print(f'los enteros"{existe}" existen en la lista y son en total: {len(interger)}')
    else:
        print("no existen")

# 6. recorrer en for flotantes y validar si el 78.0 y 45.23 si no existe y la cantidad en caso de que exista 0
existefloat = [78.0,45.23]
for floats in existefloat:
    if floats in flotantes:
        print(f'Estos flotantes {floats} estan en la lista y son en total: {len(flotantes)}')
    else:
        print(f'no existen')

# 7. recorrer en for booleanos y validar  la cantidad  de true y false en caso de que exista 0

contarTrue = 0
contarFalse = 0

for booleano in booleanos:
    if booleano == True:
        contarTrue += 1
    else:
        contarFalse += 1

print(f"En la lista booleanos, la cantidad de True es: {contarTrue} y de False es: {contarFalse}")


# 8. recorrer en for Mixta y validar si nombre y apellido son iguales en caso de que coincida un mensaje que indique que la persona se encontro
## luego comparar la edad y enviarle un mensaje de es mayor de edad o menor de edad segun el caso
# validar si el numero de telefono =  12552241  esta presente o no 
mixta = ["pepito", "perez", 25, "veeronfrng", 12552241, True]

nombre_apellido = mixta[:2]  # Obtenemos los dos primeros elementos que son el nombre y el apellido de la lista


for persona in mixta:
    if persona in nombre_apellido and nombre_apellido[0] == nombre_apellido[1]: # Verificamos nombre y apellido son iguales
        print("La persona se encontró.")
        break
else:
    print("La persona no se encontró.")

# Comparamos la edad y mostramos si es mayor o menor de edad
for persona in mixta:
    if isinstance(persona, int):  # Verificamos si el elemento es de tipo entero (edad)
        edad = persona
        if edad >= 18:
            print("Es mayor de edad.")
        else:
            print("Es menor de edad.")
        break

# Validamos si el número de teléfono está presente o no
for persona in mixta:
    if isinstance(persona, int) and persona == 12552241:
        print("El número de teléfono está presente.")
        break
else:
    print("El número de teléfono no está presente.")

## NOTA:  Es de malas practicas solucionar problemas de codigo con pocicionamiento