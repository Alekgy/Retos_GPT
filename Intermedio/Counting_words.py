"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que lea un archivo de texto y determine la frecuencia de cada palabra en el archivo. Luego, tu programa debe imprimir las 10 palabras más comunes en orden descendente de frecuencia.

    Tu programa debe ignorar los caracteres de puntuación y no debe distinguir entre mayúsculas y minúsculas.
"""

    
import string

def word(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.split()

    freq = {}
    for word in text:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    palabras_comunes = sorted(freq, key=freq.get, reverse=True)[:10]

    print("Las 10 palabras más comunes son:")
    for palabra in palabras_comunes:
        print(f"{palabra}: {freq[palabra]}")

if __name__ == '__main__':
    print(' ')
    text = input('Ingresa un texto extenso: ')
    word(text)