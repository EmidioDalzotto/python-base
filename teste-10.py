"""
exercício 010
crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar

considere 
US$1.00 = R$5.64
"""
carteira = float(input("Quantos reais você possui? R$"))
cotação = (carteira / 5.64)
print(f"Com R${carteira}, você pode adquirir US${cotação:.2f}!")