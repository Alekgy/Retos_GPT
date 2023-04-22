"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que reciba un número entero positivo y verifique si es un número de Armstrong.

    Un número de Armstrong es aquel que es igual a la suma de sus propios dígitos elevados al número total de dígitos.

    Por ejemplo, 153 es un número de Armstrong ya que 1^3 + 5^3 + 3^3 = 153.

    Tu programa debe imprimir "Sí es un número de Armstrong" si el número ingresado es de Armstrong, y "No es un número de Armstrong" en caso contrario.
"""


def run(user):
    number = []
    list = []
    for x in user: 
        number.append(int(x))
    
    for i in number:
        i = i ** len(number)
        list.append(i)
        result = sum(list)
    
    if int(user) == result:
        print(f'El numero "{user}" si es un numero Armstrong!')
    
    else:
        print(f'El numero "{user}" no es un numero Armstrong!')

        
        


if __name__ == '__main__':
    print(' ')
    user = input('Ingresa un numero: ')
    run(user)