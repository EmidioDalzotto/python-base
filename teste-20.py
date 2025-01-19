"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
e mostre a ordem sorteada

"""

import random

a1 = input("Digite o nome de um dos alunos: ")
a2 = input("Digite o nome de outro aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do último aluno: ")

alunos = [a1, a2, a3, a4]

random.shuffle(alunos)

print("A ordem de apresentação será: ")
print(f"{alunos}")
