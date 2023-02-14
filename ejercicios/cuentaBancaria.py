class cuentaBancaria:
    def __init__(self, numero_cuenta, propietarios , balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, valor):
        self.balance += valor

    def retirar(self, restar):
        self.balance