"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- menor que 16.9: muio abaixo do peso;
- entre 17 e 18.4: abaixo do peso
- entre 18.5 e 24.9: peso ideal;
- de 25 a 29.9: acima do peso;
- de 30 até 34.9: obesidade grau I;
- de 35 a 40: Obesidade grau II;
- acima de 40: obesidade grau III.
"""

print("Bem vindo! Vamos cálcular seu IMC?!")
a = float(input("Informe sua altura em metros: "))
p = float(input("Informe seu peso em kg: "))
IMC = p / (a ** 2)
print("Cálculando...")
print(f"Seu IMC é {IMC:.2f}!")
if IMC <= 16.9:
    print("Você está muito abaixo do peso ideal!")
elif IMC >= 17 and IMC <= 18.4:
    print("Você está abaixo do peso ideal!")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Você está com o peso ideial!")
elif IMC >= 25 and IMC <= 29.9:
    print("Voccê está um pouco acima do peso!")
elif IMC >= 30 and IMC <= 34.9:
    print("Você está em um quadro de obesidade grau I!")
elif IMC >= 35 and IMC <= 40:
    print("Você está em um quadro de obesidade grau II!")
elif IMC > 40:
    print("Você está em um quadro de obesidade grau III!")

