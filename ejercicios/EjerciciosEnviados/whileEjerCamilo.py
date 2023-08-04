import time 

while True:
    time.sleep(1)
    print("====Menu de opciones====")
    print("Por favor escoge UNA de estas tres opciones o ingresa '3' para salir")
    print("1. Comenzar programa")
    print("2. Imprimir listado")
    print("3. Finalizar programa")
    opcion=int(input("ingresa numero: "))
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
