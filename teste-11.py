"""
Exercício 011
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2m²
"""
a = float(input("Qual é a altura da parede em metros: "))
l = float(input("Qual é a largura da parede em metros: "))
litros = (l * a) / 2
print(f"Para pintar a área desejada será necessário {litros:.2f} litros de tinta!")