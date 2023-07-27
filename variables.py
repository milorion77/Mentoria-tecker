## las variables son contenedores para almacenar valores de datos
## creacion de variable
##python no tiene ningun comando o tipo de dato para declarar una variable
## Una variable se crea en el momento en que se le asigna un valor por primera vez
carro="hola" # esto es una cadena de texto
caracter='1'
##"" , '' cadenas de texto
# las cadenas "" molillas dobles
# los caracteres ''  comillas simples

##py no es necesario declarar las varianles con ningun tipo de 
##incluso podemos cambiar el tipo de dato despues de que se establezca
##obtener el tipo
# podemos obtener el tipo de dato de una variable con type()
print(type(carro))
print(type(caracter))
entero=45
Entero=99
decimal=45.25
boolean=45<5
boolean2=True
boolean3=False
print(type(entero))
print(type(Entero))
print(type(decimal))
print(type(boolean))
print(type(boolean2))
print(type(boolean3))
##distingue entre mayusculas y minusculas 
print(Entero)
print(entero)
## Camel case
registroPersona= "Juan" ##es la que usan ls empresas poner cuidado
#x,y,z,m=2# variables contadoras
#nombres variables, funciones  -> salarioBruto, salarioNeto, salarioTotal, suma, resoyestas
## pascal case
## pascal case es para: nombramiento de clases, nombre de archivos
#class RegistroPersonal
# serpiente: registro_Empleado  (no es la mas recomendable para usar ya que visualmente nos podemos enredar)
registro_Empleado="Maria"
## nombre de variables
## un nombre siempre comienza con una letra o "_" guion bajo
# 1manzana esto es unj error porque python entiende que estas sumandoles un 1 a una manzana, sumar un int con un string
print("manzana",1)

##valores multiples
## si son tres variables, el print pide 3 valores
contador,valor,registroUsuario=0,100,"hola"
print(contador)
print(valor)
print(registroUsuario)

##un solo valor a multiples Variables
contador=i=j=0
print(contador,i,j) 

