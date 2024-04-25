import random

def buscar_numero(lista, alvo):

    for num in lista:
        if num == alvo:
            return True
    return False

# Testando a função com diferentes listas e números alvos
lista1 = random.sample(range(100), 60)
alvo1 = 3
print(f"O número {alvo1} está presente na Lista 1? {buscar_numero(lista1, alvo1)}")
print(sorted(lista1))