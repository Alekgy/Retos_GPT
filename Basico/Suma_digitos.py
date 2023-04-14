"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que calcule la suma de los dígitos de un número entero
    positivo que ingrese el usuario. Si el número ingresado no es un entero positivo, el
    programa debe mostrar un mensaje de error.

    Por ejemplo, si el usuario ingresa el número 1234, el programa debe imprimir la suma
    de los dígitos, que es 10 (1 + 2 + 3 + 4).
"""


def run(user_number):
    try:
        number = []
        for x in user_number:
            number.append(x)
            number = [int(x) for x in number]
        result = sum(number)
        print(f'La suma de la cadena ingresada es {result}')
    except ValueError:
        print('ingresa un valor numerico')

if __name__ == '__main__':
    print(' ')
    user_number = input('Ingresa una cadena de numeros: ')
    run(user_number)