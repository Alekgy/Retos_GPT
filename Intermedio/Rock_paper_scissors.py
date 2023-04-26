"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que simule el juego de piedra, papel o tijeras.

    El programa debe pedir al usuario que elija una opción: piedra, papel o tijeras. Luego, el programa debe elegir una opción al azar (usando la librería random) y determinar quién ganó el juego, o si hubo un empate.
    
    Las reglas del juego son las siguientes:
    
        La piedra gana contra las tijeras (la piedra las rompe).
        Las tijeras ganan contra el papel (las tijeras lo cortan).
        El papel gana contra la piedra (el papel la cubre).
    
    Después de determinar quién ganó el juego, el programa debe preguntar al usuario si desea jugar de nuevo. Si el usuario responde "sí" o "yes", el programa debe comenzar de nuevo. Si el usuario responde "no" o "n", el programa debe terminar.
"""
import random


def game(user):
    options = ['Piedra', 'Papel', 'Tijeras']
    result = random.choice(options)
    user = user.capitalize()
    outcomes = {
        'Piedra': {'Piedra': 'Empate', 'Tijeras': 'Victoria', 'Papel': 'Derrota'},
        'Papel': {'Piedra': 'Victoria', 'Tijeras': 'Derrota', 'Papel': 'Empate'},
        'Tijeras': {'Piedra': 'Derrota', 'Tijeras': 'Empate', 'Papel': 'Victoria'}
    }
    
    print(f'La computadora escogio {result}')
    if user == result:
        print('Tuviste un empate')
    elif outcomes[user][result] == 'Victoria':
        print('Felicidades, Ganaste')
    else:
        print('Lo siento, Perdiste')

    
    print('Quieres volver a jugar?')
    user = input()
    user = user.capitalize()
    if user == 'Si':
        print(' ')
        user = input('Elige Piedra, Papel o Tijeras: ')
        game(user)



if __name__ == '__main__':
    print(' ')
    user = input('Elige Piedra, Papel o Tijeras: ')
    game(user)
