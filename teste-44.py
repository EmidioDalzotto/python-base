"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e a condição de pagamento:
- à vista em dinheiro/débito: 10% de desconto;
- à vista no cartão crédito: preço normal;
- cartão de crédito parcelado: 10% de juros; 
"""

valor = float(input("Qual é o valor do produto: R$"))
print("""OPÇÕES DE PAGAMENTO
[1] dinheiro/cartão débito
[2] cartão de crédito em 1 parcela
[3] cartão de crédito parcelado
""")
modo_pgto = int(input("Qual será o método de pagamento?: "))

if modo_pgto == 1:
    valor -= (valor * 0.1)
    print(f"Pagando em dinheiro ou no cartão de débito, o produto"
        f" receberá um desconto de 10%, e custará R${valor:.2f}")   
elif modo_pgto == 2:
    print(f"Pagando no cartão de crédito em 1 parcela, o produto"
        f" custará R${valor:.2f}")
elif modo_pgto == 3:
    qnt_parcelas = int(input("Será em quantas parcelas? "))
    total = valor + (valor * 0.1)
    val_par = total / qnt_parcelas
    print(f"O produto que custa R${valor:.2f}, pago no cartão de"
        f"crédito em {qnt_parcelas}, custará, com juros de 10%, "
        f"R${total:.2f}, sendo o valor de cada parcela igual a "
        f"R${val_par:.2f}.")
else:
    print("Opção inválida! digite uma das opções possíveis!")
