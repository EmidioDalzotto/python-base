"""
Faça um programa que leia o ano de nascimento de um atleta e mostre
sua categoria de acordo com a sua idade:
- até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER

"""

from datetime import datetime

data_nascimento = input("Digite a data do seu nascimento (dd/mm/aaaa): ")

d_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

hoje = datetime.today()

idade = hoje.year - d_nascimento.year

if (hoje.month, hoje.day) < (d_nascimento.month, d_nascimento.day):
    idade -= 1

if idade <= 9:
    print("Este atleta está na categoria mirim.")
elif idade <= 14:
    print("Este atleta está na categoria infantil.")
elif idade <= 19:
    print("Este atleta está na categoria Junior.")
elif idade <= 20:
    print("Este atleta está na categoria sênior.")
else:
    print("Este atleta está na categoria master.")