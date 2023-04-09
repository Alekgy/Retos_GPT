
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