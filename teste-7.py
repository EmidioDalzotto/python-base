"""
exercício 017

Faça um pragrama que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo, calcule e mostre o 
comprimento da hipotenusa.
"""
import math

cat_op = float(input("Informe o comprimento do cateto oposto: "))
cat_adj = float(input("Informe o comprimento do cateto adjacente: "))
hipote = math.hypot(cat_op, cat_adj)
print(f"O triângulo com comprimentos de cateto oposto {cat_op} e cateto" 
      f" adjacente {cat_adj} tem como comprimento da hipotenusa {hipote:.2f}.")