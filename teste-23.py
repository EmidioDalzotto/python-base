"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos
separados.
ex: 
digite um número: 1834
unidade:4
dezena:3
centena:8
milhar:1
"""

import sys

num = str(input("Digite um número de até quatro digitos: "))
if len(num) < 4:
    num = num.zfill(4)
elif len(num) > 4:
    print("O número digitado possui mais que quatro digitos, tente novamente"
          " com outro número")
    sys.exit(1)
else:
    num = num
print(f"você digitou o número {num},\n"
      f"a sua unidade é: {num[3]}\n"
      f"a sua dezena é: {num[2]}\n"
      f"a sua centena é: {num[1]}\n"
      f"e o seu milhar é : {num[0]}")


"""
tratado como número inteiro

num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"você digitou o número {num},\n"
      f"a sua unidade é: {u}\n"
      f"a sua dezena é: {d}\n"
      f"a sua centena é: {c}\n"
      f"e o seu milhar é : {m}")

"""
