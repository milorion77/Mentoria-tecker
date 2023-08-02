
#Grupo integrado por:  Camilo, Sebastian y Ana Maria

def calcular_subsidio(estrato, salario):
    menu = {
        1: 0.5,
        2: 0.4,
        3: 0.3,
        4: 0.2
    }
    porcentaje_subsidiado = menu.get(estrato, 0.1)  # Por defecto, 10% para estratos distintos de 1, 2, 3 y 4
    valor_poliza = salario * 0.05
    valor_subsidio = valor_poliza * porcentaje_subsidiado
    valor_a_cubrir = valor_poliza - valor_subsidio
    return valor_poliza, valor_a_cubrir, valor_subsidio

tabla_asociados = []
total_subsidiado = 0
subsidiados_por_estrato = {1: 0, 2: 0, 3: 0, 4: 0}
otros = 0

while True:
    try:
        asociado = len(tabla_asociados) + 1
        estrato = int(input(f"\nIngrese el estrato del asociado {asociado}: "))
        salario = float(input(f"Ingrese el salario del asociado {asociado}: "))
        valor_poliza, valor_a_cubrir, valor_subsidio = calcular_subsidio(estrato, salario)

        print(f"\nValor de la póliza para el asociado {asociado}: {valor_poliza:.2f}")
        print(f"Valor que debe cubrir el asociado {asociado}: {valor_a_cubrir:.2f}")
        print(f"Valor subsidiado por el Fondo para el asociado {asociado}: {valor_subsidio:.2f}")

        total_subsidiado += valor_subsidio
        if estrato > 4:
            otros += 1
        else:
            subsidiados_por_estrato[estrato] += 1

        tabla_asociados.append((asociado, estrato, salario, valor_poliza, valor_subsidio, valor_a_cubrir))

        continuar = input("\n¿Desea ingresar los datos de otro asociado? (y/n): ").lower()

        if continuar != "y":
            break
    except ValueError:
        print("Ingrese un valor válido.")

# Mostrar tabla con resultados
print("\nTabla de Resultados:")
print("Asociado\tEstrato\tSalario\tValor Póliza\tValor Subsidio\tValor Asociado")
print("--------------------------------------------------------------------")
for asociado, estrato, salario, valor_poliza, valor_subsidio, valor_a_cubrir in tabla_asociados:
    print(f"{asociado}\t\t{estrato}\t${salario:.2f}\t${valor_poliza:.2f}\t\t${valor_subsidio:.2f}\t\t${valor_a_cubrir:.2f}")

# Resumen
print("\nResumen:")
print("-----------")
for estrato, cantidad in subsidiados_por_estrato.items():
    print(f"Subsidios entregados para el estrato {estrato}: {cantidad}")
print(f"Otros (estratos mayores a 4): {otros}")
print(f"Monto total por subsidios desembolsado por el Fondo: ${total_subsidiado:.2f}")
print(f"Promedio subsidiado por asociado: ${total_subsidiado / len(tabla_asociados):.2f}")

