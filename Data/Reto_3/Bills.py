"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que lea un archivo CSV que contenga datos sobre los gastos de una empresa. Cada fila del archivo debe contener información sobre un solo gasto, con campos para la fecha del gasto, el concepto del gasto, el monto y la categoría del gasto.
    El programa debe ser capaz de realizar las siguientes tareas:

    - Leer los datos del archivo CSV y almacenarlos en una estructura de datos adecuada.
    - Calcular el total de gastos por categoría.
    - Calcular el promedio de gastos diarios.
    - Calcular el promedio de gastos por categoría.
    - Identificar los conceptos de gastos que más se repiten y calcular su porcentaje con respecto al total de gastos.
"""

import csv
from collections import defaultdict

gastos_por_categoria = defaultdict(float)

conceptos_de_gastos = []

cantidad_de_gastos_por_dia = defaultdict(int)

with open('gastos.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    encabezados = next(lector_csv)

    for fila in lector_csv:
        fecha = fila[0]
        concepto = fila[1]
        monto = float(fila[2])
        categoria = fila[3]

        gastos_por_categoria[categoria] += monto
        conceptos_de_gastos.append(concepto)
        cantidad_de_gastos_por_dia[fecha] += 1

total_de_gastos = sum(gastos_por_categoria.values())
promedio_de_gastos_diarios = total_de_gastos / len(cantidad_de_gastos_por_dia)
promedio_de_gastos_por_categoria = {categoria: gastos_por_categoria[categoria] / len(gastos_por_categoria) for categoria in gastos_por_categoria}

conceptos_mas_comunes = [concepto for concepto in set(conceptos_de_gastos) if conceptos_de_gastos.count(concepto) > 1]
porcentaje_conceptos_mas_comunes = sum(gastos_por_categoria[concepto] for concepto in conceptos_mas_comunes) / total_de_gastos

print(f'Total de gastos: {total_de_gastos}')
print(f'Promedio de gastos diarios: {promedio_de_gastos_diarios:.2f}')

print('Total de gastos por categoría:')
for categoria, total in gastos_por_categoria.items():
    print(f'{categoria}: {total}')

print('Promedio de gastos por categoría:')
for categoria, promedio in promedio_de_gastos_por_categoria.items():
    print(f'{categoria}: {promedio:.2f}')

print(f'Porcentaje de los conceptos de gastos más comunes: {porcentaje_conceptos_mas_comunes:.2f}%')
