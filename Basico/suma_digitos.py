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