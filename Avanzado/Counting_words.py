"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que lea un archivo de texto y calcule la frecuencia de aparición de cada palabra en el archivo. El programa debe imprimir las 10 palabras más frecuentes, junto con su frecuencia.

    Para hacerlo más interesante, puedes implementar las siguientes funcionalidades adicionales:

    Ignorar palabras comunes, como "el", "la", "y", "o", etc.
    Ignorar palabras cortas, como "a", "de", "en", etc.
    Convertir todas las palabras a minúsculas antes de contar su frecuencia.
    Mostrar las palabras en orden alfabético o por frecuencia descendente.
"""
import string

def ignore(content):
    content = content.split()
    ignore_words = ['es', 'le', 'y', 'o', 'ha', 'han', 'que', 'son','a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 'mediante', 'para', 'por', 'según', 'sin', 'sobre', 'tras', 'versus', 'vía','el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'lo', 'se', 'como', 'más' ]
    
    leaked_words = [word for word in content if word.lower() not in ignore_words]
    filtered_string = " ".join(leaked_words)
    counting(filtered_string)



def counting(filtered_string):
    words = filtered_string
    words = words.translate(str.maketrans('', '', string.punctuation))
    words = words.split()

    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    common_words = sorted(freq, key=freq.get, reverse=True)[:10]

    print("Las 10 palabras más comunes son:")
    for result in common_words:
        print(f"{result}: {freq[result]}")


if __name__ == '__main__':
    file = open("tec.txt", "r")
    content = file.read()
    ignore(content)