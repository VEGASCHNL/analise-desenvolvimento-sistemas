from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self):
        self.matricula = None
        self.salario = None

    def bater_ponto(self):
        print("Ponto batido!!!")

    def fazer_login(self):
        print("Login efetuado!!!")