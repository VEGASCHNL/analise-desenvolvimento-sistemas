import random
import os
import datetime as dt

print("=[TESTE BIBLIOTECA RANDOM]=================================")
print(" ")

print(f"RANDINT: {random.randint(0,100)}")
print(f"CHOISE: {random.choice([1, 10, -1, 100])}")
print(f"SAMPLE: {random.sample(range(1000), k=12)}")
print(" ")
print(" ")


print("=[TESTE BIBLIOTECA OS]=====================================")
print(" ")

print(f"GET CWD: {os.getcwd()}")
print(f"LIST DIR: {os.listdir()}")
print(f"CPU COUNT: {os.cpu_count()}")
print(f"GET LOGIN: {os.getlogin()}")
print(f"GET ENV: {os.getenv(key='path')}")
print(f"GET PID: {os.getpid()}")
print(" ")
print(" ")


print("=[TESTE BIBLIOTECA DATETIME]===============================")
print(" ")

hoje = dt.datetime.today()
ontem = hoje - dt.timedelta(days=1)
uma_semana_atras = hoje - dt.timedelta(weeks=1)
agora = dt.datetime.now()
duas_horas_atras = agora - dt.timedelta(hours=2)


print("Hoje é dia: ", hoje)
print("Data de ontem: ", ontem)
print("Uma semana atrás: ", uma_semana_atras)
print("Agora é: ", agora)
print("Duas horas atrás: ", duas_horas_atras)

# Formatação
hoje_formatado = dt.datetime.strftime(hoje,"%d/%m/%Y")
print(" ")
print("Hoje formatado é: ", hoje_formatado)

ontem_formatado = dt.datetime.strftime(ontem, "%d de %b de %Y")
print(" ")
print(ontem_formatado)

# Conversão
data_string = "23/05/2024 20:00"
data_dt = dt.datetime.strptime(data_string,"%d/%m/%Y %H:%M")
print(" ")
print("Data convertida: ", data_dt)