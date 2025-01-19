"""
Escreva um programa que leia dois números inteiros e os compare, 
mostrado na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.

"""

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    print("O primeiro valor é maior.")
elif a < b:
    print("O segundo valor é maior.")
elif a == b:
    print("Não exite valor maior, os dois são iguais")