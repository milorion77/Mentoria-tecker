##TALLER: CICLO MIENTRAS Y SELECTOR MÚLTIPLE
# El Fondo de empleados del ITM ha decidido subsidiar una póliza de salud a sus asociados. El valor
# de la póliza es
# el equivalente al 5% del Salario Básico del asociado. El valor subsidiado por el Fondo dependerá
# del estrato del
# asociado así:
# Estrato:
# 1. 50%
# 2. 40%
# 3. 30%
# 4. 20%
# Otro. 10%
# El programa debe mostrar a cada asociado:
# a. El valor de la póliza
# b. El valor que debe cubrir el asociado
# c. El valor subsidiado por el Fondo
# El programa debe mostrar un resumen al final indicando:
# a. Cuantos subsidios se entregaron por cada estrato
# d. El monto total por subsidios que debe desembolsar el Fondo
# e. El promedio subsidiado por asociado (promedio general)

# Resolvemos en un ciclo while para recorrer la lista en lo primero: multiplicar por # el equivalente al 5% del Salario Básico del asociado. El valor subsidiado por el Fondo dependerá del estrato del asociado
# DATOS DE PRUEBA

# Asociado Estrato Salario Valor Póliza Valor subsidio Valor Asociado

 

# itmdatos = ["asociado","estrato","salario","valorPoliza","valorsubsidio","valorAsociado"]

itm = [
    {
        "Asociado":1,
        "Estrato":1,
        "Salario":1200000,
        "Valor Poliza": 60000,
        "Valor subsidio": 30000,
        "Valor Asociado": 30000
    },
    {
        "Asociado":2,
        "Estrato":2,
        "Salario":1500000,
        "Valor Poliza": 75000,
        "Valor subsidio": 30000,
        "Valor Asociado": 45000
    },
    {
        "Asociado":3,
        "Estrato":1,
        "Salario":1300000,
        "Valor Poliza": 65000,
        "Valor subsidio": 32500,
        "Valor Asociado": 32500
    },
    {
        "Asociado":4,
        "Estrato":4,
        "Salario":2800000,
        "Valor Poliza": 140000,
        "Valor subsidio": 28000,
        "Valor Asociado": 112000
    },
    {
        "Asociado":5,
        "Estrato":3,
        "Salario":2100000,
        "Valor Poliza": 105000,
        "Valor subsidio": 31500,
        "Valor Asociado": 73500
    },
    {
        "Asociado":6,
        "Estrato":5,
        "Salario":3200000,
        "Valor Poliza": 160000,
        "Valor subsidio": 16000,
        "Valor Asociado": 144000
    },
    {
        "Asociado":7,
        "Estrato":6,
        "Salario":3800000,
        "Valor Poliza": 190000,
        "Valor subsidio": 19000,
        "Valor Asociado": 171000
    },
    {
        "Asociado":8,
        "Estrato":2,
        "Salario":2000000,
        "Valor Poliza": 100000,
        "Valor subsidio": 40000,
        "Valor Asociado": 60000
    }
]

# RESUMEN (Si el programa está bien deberá mostrar estor resultados al final)

# Subsidios entregados por estrato:

# 1. 2

# 2. 2

# 3. 1

# 4. 1

# Otro. 2

# Total a desembolsar por subsidio: $227.000

# Promedio subsidiado por asociado: $28.375

# Función para calcular el subsidio según el estrato
def calcular_subsidio(estrato, valor_poliza):
    switcher = {
        1: valor_poliza * 0.5,
        2: valor_poliza * 0.4,
        3: valor_poliza * 0.3,
        4: valor_poliza * 0.2,
    }
    return switcher.get(estrato, valor_poliza * 0.1)

# Pedimos al usuario ingresar los datos de los asociados
itmDatos = []
while True:
    try:
        asociado = int(input("Ingrese el número de asociado (o 0 para terminar): "))
        if asociado == 0:
            break
        estrato = int(input("Ingrese el estrato del asociado: "))
        salario = float(input("Ingrese el salario del asociado: "))

        itmDatos.append({"Asociado": asociado, "Estrato": estrato, "Salario": salario})
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")

# Inicializamos las variables para el resumen
total_subsidio = 0
contadores_subsidio = {1: 0, 2: 0, 3: 0, 4: 0, "Otro": 0}

# Resolvemos con el ciclo while
i = 0
while i < len(itmDatos):
    salario = itmDatos[i]["Salario"]
    valor_poliza = salario * 0.05
    
    # Calculamos el valor subsidiado según el estrato
    estrato = itmDatos[i]["Estrato"]
    valor_subsidio = calcular_subsidio(estrato, valor_poliza)

    # Calculamos el valor a cubrir por el asociado
    valor_asociado = valor_poliza - valor_subsidio

    # Actualizamos los valores en el diccionario y en el resumen
    itmDatos[i]["Valor Poliza"] = valor_poliza
    itmDatos[i]["Valor subsidio"] = valor_subsidio
    itmDatos[i]["Valor Asociado"] = valor_asociado
    total_subsidio += valor_subsidio
    contadores_subsidio[estrato] += 1

    i += 1

# Imprimimos los datos de cada asociado
print("Datos de los asociados:")
print("Asociado | Valor Póliza | Valor Asociado | Valor Subsidio")
i = 0
while i < len(itmDatos):
    asociado = itmDatos[i]["Asociado"]
    valor_poliza = itmDatos[i]["Valor Poliza"]
    valor_asociado = itmDatos[i]["Valor Asociado"]
    valor_subsidio = itmDatos[i]["Valor subsidio"]
    print(f"{asociado} | ${valor_poliza:,.0f} | ${valor_asociado:,.0f} | ${valor_subsidio:,.0f}")
    i += 1

# Imprimimos el resumen
print("\nResumen:")
for estrato, cantidad in contadores_subsidio.items():
    if estrato == "Otro":
        print(f"Otro. {cantidad}")
    else:
        print(f"{estrato}. {cantidad}")

print(f"Total a desembolsar por subsidio: ${total_subsidio:,.0f}")

# Calculamos el promedio subsidiado por asociado
promedio_subsidio = total_subsidio / len(itmDatos)
print(f"Promedio subsidiado por asociado: ${promedio_subsidio:,.0f}")
