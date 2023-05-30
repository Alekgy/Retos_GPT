"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que lea un archivo CSV que contenga datos sobre los resultados de las pruebas de un examen. Cada fila del archivo debe contener información sobre un solo estudiante, con campos para el nombre del estudiante, su edad, su género, su puntuación en la prueba y la fecha de la prueba.

    El programa debe ser capaz de realizar las siguientes tareas:

    Leer los datos del archivo CSV y almacenarlos en una estructura de datos adecuada.
    Calcular el promedio de puntuaciones de los estudiantes.
    Calcular el promedio de puntuaciones de los estudiantes por género.
    Calcular el porcentaje de estudiantes que aprobaron la prueba (con una puntuación mayor o igual a 60).
    Calcular el porcentaje de estudiantes que aprobaron la prueba por género.
"""

import csv

datos = []
puntuaciones = []
puntuaciones_genero = {'M': [], 'F': []}
aprobados = []
aprobados_genero = {'M': [], 'F': []}

with open('resultados.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    encabezados = next(lector_csv)
    for fila in lector_csv:
        datos.append(fila)
        puntuaciones.append(int(fila[3]))
        puntuaciones_genero[fila[2]].append(int(fila[3]))
        if int(fila[3]) >= 60:
            aprobados.append(fila)
            aprobados_genero[fila[2]].append(fila)

promedio_puntuaciones = sum(puntuaciones) / len(puntuaciones)

promedio_puntuaciones_genero = {'M': sum(puntuaciones_genero['M']) / len(puntuaciones_genero['M']),
                                'F': sum(puntuaciones_genero['F']) / len(puntuaciones_genero['F'])}

porcentaje_aprobados = len(aprobados) / len(datos) * 100

porcentaje_aprobados_genero = {'M': len(aprobados_genero['M']) / len([fila for fila in datos if fila[2] == 'M']) * 100,
                               'F': len(aprobados_genero['F']) / len([fila for fila in datos if fila[2] == 'F']) * 100}

print(f'Promedio de puntuaciones: {promedio_puntuaciones:.2f}')

print(f'Promedio de puntuaciones por género: M: {promedio_puntuaciones_genero["M"]:.2f}, F: {promedio_puntuaciones_genero["F"]:.2f}')

print(f'Porcentaje de estudiantes que aprobaron la prueba: {porcentaje_aprobados:.2f}%')

print(f'Porcentaje de estudiantes que aprobaron la prueba por género: M: {porcentaje_aprobados_genero["M"]:.2f}%, F: {porcentaje_aprobados_genero["F"]:.2f}%')
