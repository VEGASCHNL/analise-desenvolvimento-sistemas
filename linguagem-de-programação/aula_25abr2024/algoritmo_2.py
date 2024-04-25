import random

def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            print("Deu Bom!!!")
            break
        else:
            print("Deu Ruim!!!")
            break

lista = random.sample(range(1000), 50)
print(sorted(lista))

executar_busca_linear(lista,10)