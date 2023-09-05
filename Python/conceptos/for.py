#for element in mixta:
## se usa para iterar sobre una secuencia 
## for 
mixta=["pepito","perez",25,"veeronfrng",12552241,True]
for elemeto in mixta:
    print(elemeto)

for element in "amor":
    if element in ["a","e","i","o","u"]:
        print(" es una vocal")
print()
for x in range(6):
    print(x)
print()
for x in range(2,6):
    print(x)
print()
for x in range(2,30,5):
    print(x)
mixta1=["hola","jkjdh","djdj"]
interger=[78,45,23,11,10,98]
for x in mixta1:
  for y in interger:
   print(y)

## escribir un programa para calcular el costo de los articulos de todos los articulos de un carrito de compras
## lista de  10 ,20, 30

lista=[10,20,30]
totalA=0
for precio in lista:
    totalA+=precio
    print(f"total: {totalA} articulos" )

## vamos a escribir un codigo para dibujar f
numeros=[5,2,5,2,2]
for count in numeros:
    salida=''
    for count1 in range(count):
        salida+='x'
    print(salida)

##escribir un programa que pida al usuario (un input) un numero entero y muestre por pantalla un triangulo rectangulo
## con altura del numero introducido y debe de quedar asi:
'''
*
**
***
*****
'''

altura = int(input("Digita la altura para el triangulo: "))
for medida in range(altura +1):
    for i in range (medida) :
        print("*", end="")
    print()


## escriba un programa que pida al usuario un numero entero y muestre por pantalla 
# un triangulo rectangulo con la altura del numero introducido
'''
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''
alturaNum = int(input("Digita la altura para el triángulo: "))

for impar in range(1, alturaNum * 2, 2):
    for patras in range(impar, 0, -2):
        print(patras, end=" ")
    print()


## escribir un programa que muestre  por pantalla  las tablas de multiplicar del 1 al 10 
inputcito= int(input("Coloca el numero que quiera multiplicar hasta 10 :) : "))
for numero in range(1, inputcito+1):
    print(f"Tabla del {numero}:")
    for numero2 in range(1, 11):
        resultado = numero * numero2
        print(f"{numero} x {numero2} = {resultado}", end="   ")
    print()
