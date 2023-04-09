
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