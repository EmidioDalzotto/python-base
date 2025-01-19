"""
Exercício 018
Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo

"""

import math

angulo_graus = float(input("Digite quatos graus tem o ângulo: "))

angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"O ângulo {angulo_graus} tem como seno {seno:.2f}, cosseno {cosseno:.2f}"
      f" e tangente {tangente:.2f}.")