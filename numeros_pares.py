"""
Faça um programa que imprime os números pares de 1 a 200
e pula os números ímpares


"""
n = 0
while n <201:
    n = n+1
    if n%2 == 0:
        print(n)


for num in range(1,201):
    if num % 2 != 0:
        continue
    print(num)


