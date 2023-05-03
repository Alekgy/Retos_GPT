"""
    DESCRIPCION DEL RETO INTERMEDIO:

    Crea una clase Banco que tenga los siguientes atributos:

    nombre (str)
    lista_cuentas (list)
    saldo_total (float)

La lista de cuentas será una lista de objetos de la clase Cuenta que tendrán los siguientes atributos:

    numero_cuenta (str)
    cliente (str)
    saldo (float)

La clase Banco deberá tener los siguientes métodos:

    agregar_cuenta: agrega una nueva cuenta a la lista de cuentas del banco.
    buscar_cuenta: busca una cuenta por su número de cuenta y devuelve el objeto de la cuenta.
    depositar: recibe como parámetros el número de cuenta y la cantidad a depositar y actualiza el saldo de la cuenta correspondiente.
    retirar: recibe como parámetros el número de cuenta y la cantidad a retirar y actualiza el saldo de la cuenta correspondiente. Si la cantidad a retirar es mayor al saldo de la cuenta, se debe imprimir un mensaje de error.
"""

class Bank:
    name = str
    list_account = list
    total_balance = float

    def __init__(self, name, total_balance):
        self.name = name
        self.total_balance = total_balance
        self.list_account = self.Account()

    class Account:
        account_number = str
        client = str
        balance = float

        def __init__(self):
            pass


    def add_account(self):
        pass

    def find_account(self):
        pass

    def deposit(self):
        pass

    def withdraw(self):
        pass