"""
crie um programa que leia o nome de uma pessoa e diga se ela tem
'SILVA' no nome.
"""
nome = str(input("Qual é o seu nome? "))
nome = nome.upper()

if nome.find("SILVA") != -1:
    print("Que legal, você tem SILVA no nome.")
else:
    print("Você não tem SILVA no nome.")
