"""
    DESCRICPCION DEL RETO:

   Supongamos que tienes un archivo de texto que contiene información de ventas de productos en diferentes tiendas. Cada línea del archivo representa una venta y tiene el siguiente formato: id_tienda,fecha,producto,cantidad,precio_unitario.

    Tu tarea es procesar este archivo utilizando Pyspark y responder las siguientes preguntas:

    - ¿Cuántas tiendas aparecen en el archivo?
    - ¿Cuál es el total de ventas para cada producto?
    - ¿Cuál es el total de ventas para cada tienda?
    Para resolver este reto, puedes seguir los siguientes pasos:

    - Carga el archivo de texto en un RDD de Pyspark.
    - Utiliza la transformación map() para convertir cada línea en una tupla con los campos id_tienda, producto, cantidad y precio_unitario.
    - Utiliza la transformación distinct() para obtener un RDD con las tiendas únicas.
    - Utiliza la transformación reduceByKey() para obtener el total de ventas por producto.
    - Utiliza la transformación groupBy() y reduceByKey() para obtener el total de ventas por tienda. 
"""

from pyspark import SparkContext