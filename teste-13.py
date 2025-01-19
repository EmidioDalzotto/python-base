"""
Exercício 013
Faça um algoritmo que leia o salário de um funcionário e mostre
seu novo salário, com 15% de aumento.

"""
salário = float(input("Qual é o salário atual do funcionário: R$"))
novo_salário = salário * 1.15
print(f"Parabéns, o novo salário com aumento é de R${novo_salário:.2f}!")