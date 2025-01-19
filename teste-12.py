"""
Exercício 012
Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço,
com desconto de 5%

"""
preço = float(input("Qual o preço do produto: R$"))
novo_preço = preço * 0.95
print(f"O preço promocional de 5% é de R${novo_preço:.2f}")