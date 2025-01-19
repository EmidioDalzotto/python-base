"""
Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. O programa va perguntar o valor da casa, o salário do 
comprador e em quantos anos ele vai pagar.
Em seguida, vai calcular o valor da prestação mensal, sabendo que ela
não pode exceder 30% do salário ou então o empréstimo será negado.

"""


# minha resolução

valor_casa = float(input("Informe o valor total do imóvel a ser financiado: R$"))
salario = float(input("Informe o valor o seu salário: R$"))
tempo_pgto = int(input("Por favor, informe em números em quantos anos" )
                         " pretende pagar o financiamento: ")

valor_prestacao = float(valor_casa) / (float(tempo_pgto) * 12)

print(f"O empréstimo solicitado foi no valor de {valor_casa}, para"
      f" pagamento no prazo de {tempo_pgto} anos.")
if valor_prestacao > (float(salario) * 0.3):
    print("Infelizmente seu empréstimo foi negado.")
else:
    print("Parabés, seu empréstimo foi aprovado o valor da prestação"
          f" será de {valor_prestacao:.2f} reais por mês.")

# resolução do professor

casa = float(input("Valor da casa: R$"))
salário = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento?: "))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}.'.format(prestação))
if prestação <= mínimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")
