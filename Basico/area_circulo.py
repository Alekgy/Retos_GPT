"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que calcule el área y el perímetro de un círculo a
    partir del radio ingresado por el usuario.

    Tu programa debe mostrar el área y el perímetro con dos decimales de precisión.

    Recuerda que el área de un círculo se calcula como A = pi * r^2 y el perímetro
    como P = 2 * pi * r, donde r es el radio y pi es una constante con un valor
    aproximado de 3.14159.
"""


pi = 3.14159


def area(user):    
    result = pi * user ** 2
    result = round(result, 2)
    print(f'El area del radio {user} es {result}')


def perimetro(user):
    result = 2 * pi *user
    result = round(result, 2)
    print(f'El perimetro de {user} es {result}')



if __name__ == '__main__':
    print(' ')
    user = int(input('Ingresa el radio del circulo a hayar area y perimetro: '))
    area(user)
    perimetro(user)