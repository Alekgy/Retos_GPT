
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

