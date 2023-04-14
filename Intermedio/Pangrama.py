"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que solicite al usuario ingresar una cadena de caracteres y determine si es un pangrama o no. 
"""

chains_for_tests = [
    "El cadáver de Wamba, rey godo de España, fue exhumado y trasladado en una caja de zinc que pesó un kilo",  # No
    "Hola",  # No
    "aeiou",  # No
    "parzibyte",  # No
    "abcdefghijklmnñopqrstuvwxyz",  # Sí
    "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja",  # Sí,
    "abcdefghijklmnopqrstuvwxyz",  #No, porque no lleva ñ
    "Mi hijo degustó en el festival de bayas una extraña pizza de kiwi con queso",  #Sí
]

import string

def pangrama(text):
    chain = text.lower()
    alphabet = string.ascii_lowercase + "ñ"

    for letter in alphabet:
        if letter not in chain:
            return False
    
    return True

if __name__ == '__main__':
    print(' ')
    text = str(input('Ingresa una cadena de texto que creas que es un pangrama: '))
    if pangrama(text):
        print(f'"{text}" es un pangrama')
    else:
        print(f'"{text}" no es un pangrama!')