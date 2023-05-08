"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que lea un archivo CSV que contenga datos sobre una lista de productos. Cada fila del archivo debe contener información sobre un solo producto, con campos para el nombre del producto, la categoría, el precio y la cantidad disponible.

    - El programa debe ser capaz de realizar las siguientes tareas:

    - Leer los datos del archivo CSV y almacenarlos en una estructura de datos adecuada.

    - Permitir al usuario buscar productos por nombre o por categoría y mostrar los resultados.

    - Permitir al usuario agregar nuevos productos a la lista.

    - Permitir al usuario modificar el precio o la cantidad disponible de un producto existente.

    - Permitir al usuario guardar los cambios en el archivo CSV.

    Para hacerlo más interesante, puedes implementar algunas de las siguientes funcionalidades adicionales:

    - Validar que los campos ingresados por el usuario sean válidos (por ejemplo, que el precio sea un número válido y la cantidad disponible sea un número entero positivo).
    - Ordenar la lista de productos por nombre, precio o cantidad disponible.
    - Permitir al usuario eliminar un producto de la lista.
    - Agregar una opción para mostrar solo productos con una cantidad disponible menor que un valor dado.
    - Agregar una opción para mostrar solo productos que estén dentro de un rango de precios dado.
"""
import sqlite3
import csv

ruta_csv = '/home/alejandro/ALEJANDRO/Retos_GPT/Avanzado/Archivo.csv'
ruta_db = '/home/alejandro/ALEJANDRO/Retos_GPT/Avanzado/DB.db'

class Productos:
    def __init__(self, nombre, categoria, ruta_db):
        self.nombre = nombre
        self.categoria = categoria
        self.productos = []
        self.read(ruta_db)


    def read(self, ruta_db):
        with open(ruta_db, 'r') as archivo:
            lector_csv = csv.reader(archivo)

            for fila in lector_csv:
                nombre, categoria, precio, cantidad = fila
                self.productos.append({
                    'nombre': nombre,
                    'categoria': categoria,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })

    def search(self):
        resultados = []
        for producto in self.productos:
            if self.nombre.lower() in producto['nombre'].lower():
                resultados.append(producto)
            
            elif self.categoria.lower() == producto['categoria'].lower():
                resultados.append(producto)

        return resultados

    def add(self, nombre, categoria, precio, cantidad):

        self.productos.append({
            'nombre': nombre,
            'categoria': categoria,
            'precio': float(precio),
            'cantidad': int(cantidad)
        })

    def modify(self, precio=None, cantidad=None):

        for producto in self.productos:
            if self.nombre.lower() == producto['nombre'].lower():
                if precio is not None:
                    producto['precio'] = float(precio)
                if cantidad is not None:
                    producto['cantidad'] = int(cantidad)
                return True
        return False


def conexion(ruta_csv, ruta_db):
    conexion = sqlite3.connect(ruta_db)

    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Productos
                    (id INTEGER PRIMARY KEY,
                    Nombre TEXT,
                    Categoria TEXT,
                    Precio INTEGER,
                    Cantidad_disponible INTEGER)''')

    with open(ruta_csv, newline='') as csvfile:
        content = csv.DictReader(csvfile)
        for fila in content:
            cursor.execute('INSERT INTO Productos (Nombre, Categoria, Precio, Cantidad_disponible) VALUES (?, ?, ?, ?)', (fila['Nombre'], fila['Categoria'], fila['Precio'], fila['Cantidad_disponible']))

    conexion.commit()
    conexion.close()

def save_change():
    pass