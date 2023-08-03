## El ciclo while
## para ejecutar un conjunto de condiciones simepre que una condicion se cumpla
i=1
while i<6:
    print(f" el numero es {i}")
    i+=1

#con la instruccion break podemos detener el ciclo incluyendo si la condicion es TRUE

print("======================================================================================")
i=1
while i<=6:
    print(f" el numero es {i}")
    if i==3:
        break
    i+=1
     