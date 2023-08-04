## ejercio
# Solicitar al usuario que ingrese números 
# enteros positivos y, por cada uno, imprimir la suma 
# de los dígitos que lo componen. La condición de corte
# es que se ingrese el número -1. Al finalizar, mostrar 
# cuántos números ingresados ​​por el usuario fueron números pares.
'''
nPares=0
sumaTotal=0
numero=int(input(" ingrese el Numero (-1 para terminar el programa)"))
while numero!=-1:
    if numero%2==0:
        nPares+=1
    sumaTotal+=numero
    sumaNumeros=0
    while numero!=0:
        digito=numero%10
        sumaNumeros+=digito
        numero=numero//10
    print(" la suma de los digitos es: ",sumaNumeros)
    numero=int(input(" ingrese el Numero (-1 para terminar el programa)"))
print(f" se ingresaron {nPares} numeros pares  ")
print(f" La suma de numeros es {sumaTotal} ")

'''
##Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir 
# listado, 3-finalizar programa. A continuación, el usuario debe poder 
# seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informele
#  del error. El menú se debe volver a mostrar luego de ejecutar cada opción, 
# permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. 
# Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
'''
while True:
    print("====Menu de opciones====")
    print("Por favor escoge UNA de estas tres opciones o ingresa '3' para salir")
    print("1. Comenzar programa")
    print("2. Imprimir listado")
    print("3. Finalizar programa")
    opcion=int(input("ingresa numero "))
    if opcion==1: 
        print("Comenzando programa...")
    elif opcion==2:
         print("Imprimir listado")
    elif opcion==3:
            print("Saliendo del programa. ¡Hasta luego!")
            break
    else:
        print("Opción inválida, Escoge una de las tres opciones")
        opcion=int(input("Prueba exitosa"))
'''
print("=========================================================================================================================")
'''
##Solicitar al usuario el ingreso de una frase y de una letra 
# (que puede o no estar en la frase). Recorrer la frase, carácter a carácter,
#  comparando con la letra buscada. Si el carácter no coincide, indique que 
# no hay coincidencia en esa posición (imprimiendo la posición) y continúe.
#  Si se encuentra una coincidencia, indique en qué posición se encontró y
#  finalizó la ejecución.

frase = input("Frase: ")
letra= input("Digita la letra que quieras buscar en la frase: ")
posicion=0

while posicion!=len(frase):
     if letra != frase[posicion]:
          print("No se encontro en la posicion", posicion)
          posicion+=1
          continue
     print("Se encontro en la posicion", posicion)
     break
'''
print("=========================================================================================================================")

##Crear un programa que permita al usuario ingresar los montos de las compras 
# de un cliente (se desconoce la cantidad de datos que cargará, la cual puede 
# cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario 
# ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y 
# se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total 
# a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
# se le debe aplicar un 10% de descuento.

totalPagar= 0
while True:
    compraCliente = float(input("Ingresa el valor de tu compra "))

    if compraCliente == 0:
        break
    if compraCliente < 0:
          print("Digite un monto positivo!!!!!")
    else:
        totalPagar += compraCliente
        print(f"Valor compra hasta el momento: {compraCliente}")

if totalPagar >= 1000:
    descuento= totalPagar*0.1
    totalPagar-=descuento
     
print(f"El total a pagar es: ${totalPagar:.2f} con el descuento del 10%")
