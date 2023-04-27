"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que genere un número aleatorio entre 1 y 100, y permita al usuario adivinar el número en un máximo de 10 intentos. El programa debe proporcionar pistas al usuario después de cada intento, indicando si el número a adivinar es mayor o menor que el número ingresado. Al finalizar el juego, el programa debe imprimir el número de intentos que le llevó al usuario adivinar el número.
"""
import random

def guess():
    number = random.randint(1, 100)
    max_attempts = 10

    for attempt in range(max_attempts):
        print(f"Tienes {max_attempts-attempt} intentos restantes.")
        
        try:
            guess = int(input('Adivina el número entre 1 y 100: '))
        except ValueError:
            print('Ingresa un número entero válido.')
            continue
        
        if guess < number:
            print('El número es más alto.')
        elif guess > number:
            print('El número es más bajo.')
        else:
            print(f'¡Felicidades, adivinaste el número en {attempt+1} intentos!')
            break
    else:
        print(f'Lo siento, excediste los {max_attempts} intentos. El número era {number}.')
    
if __name__ == '__main__':
    print(' ')
    guess()