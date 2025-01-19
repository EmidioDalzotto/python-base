"""
crie um programa que leia o nome de uma cidade e diga se ela começa ou não
com o nome "SANTO".
"""

entrada = str(input("Digite o nome de uma cidade: ")).strip()
nome_cidade = entrada.upper()

if nome_cidade.find('SANTO') == 0:
    print('O nome da cidade começa com Santo')
else:
    print('O nome da cidade não começa com Santo')

