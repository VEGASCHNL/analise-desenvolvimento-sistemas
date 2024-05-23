from ContaCorrente import ContaCorrente

class ContaPF(ContaCorrente):
    def __init__(self):
        self.cpf = None

    def solicitar_emprestimo(self):
        print("Emprestimo Solicitado com Sucesso!")
