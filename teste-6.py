"""
Exercício 016
Crie um programa que leia um número real qualquer e mostra na tela a sua
porção inteira.

Ex:
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""

import math

n = float(input("Digite um número: "))
partint = math.floor(n)
print(f"O número {n} tem a parte inteira {partint}.")