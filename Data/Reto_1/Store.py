"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que lea un archivo CSV que contenga datos sobre ventas de una tienda. Cada fila del archivo debe contener información sobre una sola venta, con campos para la fecha, el nombre del producto, la cantidad vendida y el precio de venta.

    El programa debe ser capaz de realizar las siguientes tareas:

    Leer los datos del archivo CSV y almacenarlos en una estructura de datos adecuada.
    Calcular el total de ventas por producto.
    Calcular el total de ventas por día.
    Calcular el promedio de ventas diarias.
    Calcular el promedio de ventas por producto. 
"""

import csv
from collections import defaultdict

ventas_por_producto = defaultdict(float)
ventas_por_dia = defaultdict(float)

cantidades_por_producto = defaultdict(int)
cantidades_por_dia = defaultdict(int)

with open('ventas.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    encabezados = next(lector_csv)  

    for fila in lector_csv:
        fecha = fila[0]
        producto = fila[1]
        cantidad = int(fila[2])
        precio = float(fila[3])

        ventas_por_producto[producto] += cantidad * precio
        ventas_por_dia[fecha] += cantidad * precio

        cantidades_por_producto[producto] += cantidad
        cantidades_por_dia[fecha] += cantidad

promedio_ventas_por_producto = {producto: ventas_por_producto[producto] / cantidades_por_producto[producto] for producto in ventas_por_producto}
promedio_ventas_por_dia = {fecha: ventas_por_dia[fecha] / cantidades_por_dia[fecha] for fecha in ventas_por_dia}

total_ventas = sum(ventas_por_dia.values())
promedio_ventas_diarias = total_ventas / len(ventas_por_dia)

print(f'Total de ventas: {total_ventas}')
print(f'Promedio de ventas diarias: {promedio_ventas_diarias:.2f}')

print('Total de ventas por producto:')
for producto, total in ventas_por_producto.items():
    print(f'{producto}: {total}')

print('Total de ventas por día:')
for fecha, total in ventas_por_dia.items():
    print(f'{fecha}: {total}')

print('Promedio de ventas por producto:')
for producto, promedio in promedio_ventas_por_producto.items():
    print(f'{producto}: {promedio:.2f}')

print('Promedio de ventas por día:')
for fecha, promedio in promedio_ventas_por_dia.items():
    print(f'{fecha}: {promedio:.2f}')