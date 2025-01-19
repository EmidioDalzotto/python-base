"""
exercício 009
de modo simples, faça uma tabuada do número informado
"""
n = int(input("Informe um número: "))
operação = (1, 2, 3, 4, 5, 6, 7, 8 ,9, 10)

print("{:-^40}".format(f"TABUADA DO {n}"))

for numero in operação:
    resultado = numero * n
    print(f"{n} x {numero} = {resultado}")

 