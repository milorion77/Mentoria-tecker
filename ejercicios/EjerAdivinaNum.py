
'''
EJERCICIO:

Juego sencillo en Python llamado “Adivina el número”. El juego consiste en adivinar un número secreto generado por el programa.
A medida que se avanza, se observarán la implementación de conceptos básicos de Python, como variables, listas, tuplas, metodos de lista, bucles while y for y condicionales
y de más conceptos vistos hasta hoy que les puedan ayudar.
En este juego, el programa genera un número aleatorio pero este número no es visible para el jugador.
El jugador intenta adivinar el número. Si el jugador ingresa el mismo número que genera el sistema, 
el programa muestra el mensaje ganador y el juego termina allí.
Si el jugador ingresa un número incorrecto, ese número se evalúa. Si el número es mayor que la respuesta correcta, 
el sistema da una pista de que el número ingresado es 'alto'; de lo contrario, si el número es menor que la respuesta correcta, dice 'inferior'.
Hay un número limitado de intentos disponibles con el usuario para ganar el juego.
'''

'''
import random
numeroLoco = random.randint(1,5)
print(numeroLoco)
print("====ADIVINA EL NUMERO====")


contadorIntentos = 0
intentosMaximo = 3
while contadorIntentos < intentosMaximo: 
    numeroUser = int(input(f"Intento # {contadorIntentos + 1}/{intentosMaximo} Ingresa un numero entero entre ( 1, 5) para empezar a jugar (o presiona 0 para salir) "))
    if numeroUser > 5:
        print("Hey mi bro, es hasta 5, perdiste una oportunidad :v")
    if numeroUser == 0:
        print("Haciendo la salidacion...")
        break
    elif numeroLoco == numeroUser:
        print("Adininasteeee!!! que suertudo")
        break
    elif numeroLoco < numeroUser:
        print("uff te pasaste, tu numero ingresado es mayor. Intenta con uno mas pequeño ")

    elif numeroLoco > numeroUser:
        print("nahhh, tu numero ingresado es bajo. Intenta con otro mas grande")


    contadorIntentos += 1
if contadorIntentos == intentosMaximo:
    print("Ya no tienes mas intento mi bro, perdiste xD ")
'''

import random

numeroLoco = random.randint(1, 10)
print(numeroLoco)
print('''====👀ADIVINA EL NUMERO ENLOQUECIDO 
               E IMPREDECIBLE😜====''')

listaNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

intentos = 0
intentosMaximo = 3

while intentos < intentosMaximo:
    usuario = int(input(f"Intento # {intentos + 1}/{intentosMaximo} Ingresa un numero entero entre ( 1, 10) para empezar a jugar ó (o presiona 0 para salir) "))
    if usuario == 0:
        print("Gracias por jugar. Chaitoooo!")
        break
    
    if usuario in listaNum:
        intentos += 1
        for adivinoNum in listaNum:
            if usuario == numeroLoco:
                print(f"¡Felicitaciones! Adivinaste el número {numeroLoco} en {intentos} intentos. ¡Ganaste!")
                break
            elif usuario < numeroLoco:
                print("Adivina adivinador el numero que colocaste es Menor. Sigue intentando.")
                break
            else:
                print("Adivina adivinador el numero que colocaste es Mayor. Sigue intentando.")
                break
    else:
        print("Amig@ estas bien? Ese número esta fuera del rango del juego (1 al 10). Inténtalo nuevamente.")
if intentos == intentosMaximo:
    print("Ya no tienes mas intento mi bro, perdiste xD ")