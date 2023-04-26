"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que reciba una lista de números y calcule la media, la mediana y la moda.

    La media es el promedio de todos los números en la lista.
    La mediana es el número en el medio de una lista ordenada.
    La moda es el número que aparece con más frecuencia en una lista.

    Tu programa debe imprimir la media, la mediana y la moda de la lista ingresada. Si hay varios números que cumplen con la definición de moda, puedes imprimir cualquiera de ellos.
"""
from statistics import mode, median

def run(user):
    user = user.replace(' ', '')
    number = []
    for x in user:
        number.append(int(x))
    media = sum(number) / len(number) 
    print(f'La media es {media}')
    print(f'La moda es {mode(number)}')
    print(f'La mediana es {median(number)}')


if __name__ == '__main__':
    print(' ') 
    user = input('Ingresa una cadena de numeros: ')
    run(user)