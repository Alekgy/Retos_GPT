"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que le solicite al usuario que ingrese una cadena
    de caracteres y luego determine si la cadena es un palíndromo o no.
    Un palíndromo es una cadena que se lee igual de izquierda a derecha como de derecha a izquierda.

    Por ejemplo, las palabras "reconocer" y "radar" son palíndromos.
"""


def palindromo(word):
    word = word.replace(' ','')
    word = word.lower()
    inverted_word = word [::-1]
    
    if word == inverted_word:
        print('La cadena ingresada es un palindromo!')
    elif word != inverted_word:
        print('La cadena ingresada no es un palindromo!')
    

if __name__ == '__main__':
    print(' ')
    word = input('Ingresa una frase o palabra: ')
    palindromo(word)