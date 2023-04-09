"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que le solicite al usuario que ingrese un número entero
    positivo y luego calcule e imprima el factorial de ese número.

    Recuerda que el factorial de un número entero positivo n es el producto de todos Los
    números enteros positivos desde 1 hasta n.

    Por ejemplo, el factorial de 5 se calcula como 1 x 2 x 3 x 4 x 5 = 120.

"""


def factorial(user_number): 
    if user_number == 0 or user_number == 1:
        result = 1
    elif user_number > 1:
        result = user_number * factorial(user_number - 1)
    return result

if __name__ == '__main__':
    print(' ')
    user_number = int(input('Ingresa el numero que deseas conocer su factorial: '))
    result = factorial(user_number)
    print(f'El factorial de {user_number} es {result}')