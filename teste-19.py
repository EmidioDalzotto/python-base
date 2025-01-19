"""
Exercício 019

um profesor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do
escolhido.

"""
import random

a1 = input("Digite o nome de um dos alunos: ")
a2 = input("Digite o nome de outro aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do último aluno: ")

alunos = (a1, a2, a3, a4)

a_sorteado = random.choice(alunos)
print(f"O aluno escolhido para apagar o quadro foi {a_sorteado}")
