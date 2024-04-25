listagem = list(range(1,50))

def executar_busca_linear(lista,valor):

    for elemento in lista:
        if valor == elemento:
            print("Deu Certo!!!")
            break
        else:
            print("Deu Ruim")
            break

executar_busca_linear(listagem,1)