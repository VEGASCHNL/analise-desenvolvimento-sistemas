from ContaCorrente import ContaCorrente

class ContaPJ(ContaCorrente):
    def __init__(self):
        self.cnpj = None

    def sacar_emprestimo(self):
        print("Emprestimo Sacado com Sucesso!")