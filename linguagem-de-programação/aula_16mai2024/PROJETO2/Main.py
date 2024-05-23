from ContaPF import ContaPF
from ContaPJ import ContaPJ

pf = ContaPF()
pj = ContaPJ()

# DADOS CONTA CORRENTE
# PF
pf.nome = "Negreiros"
pf.email = "negreiros@negreiros.com.br"
pf.telefone = "(11) 00000-0000"
pf.saldo = 2034
pf.cpf = "000.000.000-00"


print("-------------------- CONTA (PF) --------------------")
print(pf.nome)
print(pf.email)
print(pf.telefone)
print(pf.saldo)
print(pf.cpf)

# PJ
pj.nome = "Negreiros LTDA"
pj.email = "negreiros@negreirosLTDA.com"
pj.telefone = "(11) 11111-1111"
pj.saldo = 3154737500
pj.cnpj = "11.111.111/0001-11"
print("-------------------- CONTA (PJ) --------------------")
print(pj.nome)
print(pj.email)
print(pj.telefone)
print(pj.saldo)
print(pj.cnpj)
