"""
    DESCRIPCION DEL RETO:

    Escribe un programa en Python que le solicite al usuario que ingrese un número entero
    positivo y luego determine si ese número es un número primo o no.

    Recuerda que un número primo es un número entero mayor que 1 que no tiene divisores
    distintos a 1 y a sí mismo.
"""


def es_primo(user):
    if user < 2:
        return False
    for i in range(2, user // 2 + 1):
        if user % i == 0:
            return False
    return True

def run():
    user = int(input("Escribe un número: "))
    if es_primo(user):
        print("El número ingresado es primo.")
    else:
        print("El número ingresado no es primo.")

if __name__ == "__main__":
    run()
