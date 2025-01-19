"""
exercício 008

faça um programa que leia um valor em metros e o exiba convertido em
centímetros e milímetros

"""
m = float(input("Informe o valor em metros que deseja converter: "))

cm = m * 100
mm = m * 1000

print(f"{m} m equivale à {cm} cm ou a {mm} mm.")
