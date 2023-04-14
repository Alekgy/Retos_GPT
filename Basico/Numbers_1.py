"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que le solicite al usuario que ingrese un número
    entero positivo y luego imprima todos los números pares desde 2 hasta ese número
    ingresado por el usuario.
"""


def run():
    user_number = int(input('Ingresa un numero entero: '))
    number = 0
    while number != user_number:
        print(number)
        number += 2
        if number == user_number:
            print(number)
    

if __name__ == '__main__':
    print(' ')
    run()

