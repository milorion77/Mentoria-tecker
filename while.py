## el cliclo while 
##  para ejecutar un conjunto de condiciones siempre que una condicion sea verdadera
i=1
while i<=6:
    print(f" el numero es {i}")
    i+=1
# con la instruccion break podemos detener el ciclo incluso si la condicion es true
print("---------------------------------------------")
i=1
while i<=6:
    print(f" el numero es {i}")
    if i==3:
        break
    i+=1
print("---------------------------------------------")
i=0
while i<=6:
  i+=1
  if i==3:
        continue
  print(f" el numero es {i}")
print("---------------------------------------------")
i=0
while i<=6:
  i+=1
  if i==3:
        continue
  print(f" el numero es {i}")
else:
    print("finalizo")
print("---------------------------------------------")
i=10
while i>0:
  i-=1
  if i==3:
        continue
  print(f" el numero es {i}")
print("---------------------------------------------")
i=10
while i>0:
    print(f" el numero es {i}")
    if i==3:
        break
    i-=1

 
nPares=0
sumaNumeros=0
digito=0
sumaDigito=0
numero=int(input(" ingrese el Numero (-1 para terminar el programa)"))
while numero!=-1:
    print("hola")
    if numero%2==0:
        nPares+=1
    sumaNumeros=0
    while numero!=0:
        digito=numero%10
        sumaNumeros+=digito
        numero=numero
    print(" la suma de los digitos es: ",sumaDigito)
    numero=int(input(" ingrese el Numero (-1 para terminar el programa)"))
print(f" se ingresaron {nPares} numeros pares  ")
print(f" La suma de numeros es {sumaNumeros} ")