"""
Faça um programa que leia o ano de nascimento deu um jovem e informe, de
acordo coma sua idade:
- se ele ainda vai se alistar ao serviço militar.
- se é a hora de se alistar.
- se já passou do tempo do alistamento

O programa deve também mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import datetime

nascimento = input("Informe a data do seu nascimento (dd/mm/aaaa): ")

data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

hoje = datetime.today()

idade = hoje.year - data_nascimento.year

if (hoje.month, hoje.day) < (data_nascimento. month, data_nascimento.day):
    idade -= 1

if idade < 18:
    print("Você ainda não tem idade para se alistar no serviço militar!")
    alistamento = 18 - idade
    print (f"Ainda falta(m) {alistamento} ano(s) para seu alistamento")
elif idade == 18:
    print("Está na hora de você se alistar no serviço militar!")
else:
    print("Já passou da hora do seu alistamento militar!")
    p_alistamento = idade - 18
    print(f"Seu alistamento deveria ter sido feito há {p_alistamento} ano(s)!")