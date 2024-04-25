# CALCULADORA DE IMPOSTOS

calcular_input = int(input("Digite o valor para calcular: "))

print(f"Valor Inicial: {calcular_input}")

# CALCULADORA PIS - ESTADUAL 1,65%
def calcular_pis(valor):
    imposto = 0.0165
    valor_do_imposto = (valor*imposto)
    print(f'PIS {valor_do_imposto}')


calcular_pis(calcular_input)


# CALCULADORA COFINS - ESTADUAL 7%
def calcular_cofins(valor):
    imposto = 0.07
    valor_do_imposto = (valor*imposto)
    print(f'COFINS {valor_do_imposto}')

calcular_cofins(calcular_input)

# CALCULADORA ICMS - ESTADUAL 18%
def calcular_icms(valor):
    imposto = 0.018
    valor_do_imposto = (valor*imposto)
    print(f'ICMS {valor_do_imposto}')

calcular_icms(calcular_input)