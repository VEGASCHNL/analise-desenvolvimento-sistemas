def buscar_numero(lista, alvo):

    for num in lista:
        if num == alvo:
            return True
    return False

# Testando a função com diferentes listas e números alvos
lista1 = [1, 2, 3, 4, 5]
alvo1 = 3
print(f"O número {alvo1} está presente na Lista 1? {buscar_numero(lista1, alvo1)}")

lista2 = [10, 20, 30, 40, 50]
alvo2 = 25
print(f"O número {alvo2} está presente na Lista 2? {buscar_numero(lista2, alvo2)}")

lista3 = [100, 200, 300, 400, 500]
alvo3 = 500
print(f"O número {alvo3} está presente na Lista 3? {buscar_numero(lista3, alvo3)}")