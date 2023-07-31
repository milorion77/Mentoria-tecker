## aritmeticos
# asignacion
# se utilizan para asignar valores a las variables
## ---------------------------------------------------------------------------
##          operador                                  descripcion
## ---------------------------------------------------------------------------
##          =                                      asigancion
##          +=                                    sumar y asignar
##          -=                                    restar y asignar
##          *=                                    multiplicar y asignar
##          /=                                    dividir y asignar
##          %=                                    residuo y asignar
## ---------------------------------------------------------------------------
#comparación

## Se utiliza para comparar dos valores o más

### |-----------------------------------------|

### |    operador             descripcion     |

### |-----------------------------------------|

##           ==                  Igualdad

##           !=                Desigualdad

##           <                 menor que

##           >                 mayor que

##           <=                menor igual que

##           >=                mayor igual que

### |-----------------------------------------|

valor = 45

print(valor==38) #False

print(valor==45) #True

print(valor!=78) #True

print(valor!=45) #False

print(valor<78) #True

print(valor<45) #False

 

#logicos

### |-----------------------------------------|

### |    operador             descripcion     |

### |-----------------------------------------|

##           and    retorna true ambas expresiones

##           or     retorna true si almenos uno es verdadero        

##           not    true convierte a false y viceversa

### |-----------------------------------------|

 

print(valor>14 and 12<100) # True

print(valor<14 and 12<100) # False

print(valor>14 or 12<100) #True

print(valor<14 or 12>100)# False

print(not(valor>14 and 12<100)) # False

print(not(valor>14 and 12<100))#True

#identidad

#logicos

### |-----------------------------------------|

### |    operador             descripcion     |

### |-----------------------------------------|

##           is  devuelve true si ambas variables son el mismo objeto

##         is not  devuelve tur si ambas variables NO son el mismo objeto    

### |-----------------------------------------|

 

x=["manzana","pera"]

z=["manzana","pera"]

y=x

print(x is y)# True

print(x is z)#False #guarda espacio en memoria entonces no e igual a los operadores de comparacion

print(x==y)#True

print(x!=z)#False