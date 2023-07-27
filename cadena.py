## cadenas en pyhton
# las cadenas se trabajan en "" o en '' pero en este caso lo haremos en comillas dobles 
# la funcion print para mostrar texto ""
# cadena multilinea
# podemos asignar una cadena a una variable usando 3 comillas dobles
txt="""
 es simplemente el texto de relleno de las imprentas y 
 archivos de texto. Lorem Ipsum ha sido el texto de relleno 
 estándar de las industrias desde el año 1500, cuando un impresor 
 (N. del T. persona que se dedica a la imprenta) desconocido usó una 
 galería de textos y los mezcló de tal manera que logró hacer un libro
 de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó
 como texto de relleno en documentos electrónicos, quedando esencialmente 
 igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset",
 las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de .
 autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem 
 Ipsum.
"""
print(txt)
txt1="Lorem Ipsum es simplemente el texto de relleno de las"
#Nota: en el resultado, los saltos de linea se insertan en la misma posicion que en el codigo
# las cadenas son matrices ( en peso en Bytes) asi que ojo con la administracion de estos para menor consumo de bytes
#se pueden acceder a los elementos de la cadena por corchetes []
print(txt[1])

# una cadena atraves de una ciclo
for elemento in txt:
    print(elemento)

# len() para obtener la longitud de una cadena
print(len(txt1))
# comprobar cadenas
print("simple" in txt)



txt = """
 es simplemente el texto de relleno de las imprentas y 
 archivos de texto. Lorem Ipsum ha sido el texto de relleno 
 estándar de las industrias desde el año 1500, cuando un impresor 
 (N. del T. persona que se dedica a la imprenta) desconocido usó una 
 galería de textos y los mezcló de tal manera que logró hacer un libro
 de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó
 como texto de relleno en documentos electrónicos, quedando esencialmente 
 igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset",
 las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de .
 autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem 
 Ipsum.
"""

# 1. Valide si las palabras simplemente, estándar, estandar, (.), " ", (,) existen
validar_palabra_1 = ["simplemente", "estándar", "estandar", ".", " ", ","]
for palabra in validar_palabra_1:
    if palabra in txt:
        print(f'La palabra o caracter "{palabra}" existe en el texto.')
    else:
        print(f'La palabra o caracter "{palabra}" no existe en el texto.')

# 2. Valide si las palabras juan, archivos, estan, hola, tex, " ", (,) no existen
validar_palabra_2 = ["juan", "archivos", "estan", "hola", "tex", " ", ","]
for palabra in validar_palabra_2:
    if palabra not in txt:
        print(f'La palabra o caracter "{palabra}" no existe en el texto.')
    else:
        print(f'La palabra o caracter "{palabra}" existe en el texto.')

# 3. Recorrer el texto y validar la cantidad de veces que el caracter "i" existe
contar_i = 0
for buscar in txt:
    if buscar == "i":
        contar_i += 1
print(f'El caracter "i" aparece {contar_i} veces en el texto.')

# 4. Recorrer el texto y validar la cantidad de veces que el caracter " " (espacio) existe
contar_espacio = 0
for char in txt:
    if char == " ":
        contar_espacio += 1
print(f'El caracter " " (espacio) aparece {contar_espacio} veces en el texto.')

# 5. Recorrer el texto y validar la cantidad de veces que el caracter "," (coma) existe
contar_coma = 0
for char in txt:
    if char == ",":
        contar_coma += 1
print(f'El caracter "," (coma) aparece {contar_coma} veces en el texto.')

# 6. Recorrer el texto y validar si el caracter "Lorem" no existe y la cantidad en caso de que exista es 0
contar_lorem = txt.count("Lorem")
if contar_lorem == 0:
    print('El texto no contiene la palabra "Lorem".')
else:
    print(f'La palabra "Lorem" aparece {contar_lorem} veces en el texto.')

# 6.1 jaja otra manera de acerlo con for y len
palabra_buscada = "Lorem"
contar_lorems = 0

for i in range(len(txt) - len(palabra_buscada) + 1):
    if txt[i:i+len(palabra_buscada)] == palabra_buscada:
        contar_lorems += 1

if contar_lorems == 0:
    print('El texto no contiene la palabra "Lorem".')
else:
    print(f'La palabra "Lorem" aparece {contar_lorems} veces en el texto.')

# 7. Recorrer el texto y validar si el caracter "hola" no existe y la cantidad en caso de que exista es 0
contar_hola = txt.count("hola")
if contar_hola == 0:
    print('El texto no contiene la palabra "hola".')
else:
    print(f'La palabra "hola" aparece {contar_hola} veces en el texto.')

palabra_buscada = "Lorem"

## cortar cadenas 
print(txt[:100])## no incluye el 100 -> 0,99
print("-----------------------------------------")
print(txt[100:])## no incluye el 100 -> 0,99

## negativa
b="hola, mundo!"
print(b[-5:-2])

## realizar un ejercicio basico con el random() float y vamos a cortar el numero del 1:3, inicio:6 
## cadena sacar la longitud, inicio hasta longitud
##metodos mas usados
###Upper case
## Lower case
## replace
# split
# count el de yo
# find
#format
# index
# join
# translate

