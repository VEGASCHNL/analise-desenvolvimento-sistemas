from Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self):
        self.codigo = None
        self.datacadastro = None

    def fazer_compra(self):
        print("Compra Efetuada!!!")

    def pagar_conta(self):
        print("Conta Paga!!!")