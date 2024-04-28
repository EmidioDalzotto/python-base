template = r"""
---Tabuada---
   
      {operacoes}

###################
"""

numeros = list(range(1,11))

for n1 in numeros:
    for n2 in numeros:
        operacao = f"{n1} x {n2} = {n1 * n2}"
        print(operacao)
        #print(template.format(operacoes = operacoes))