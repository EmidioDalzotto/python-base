"""
Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e
o indice de umidade do ar sendo que caso será exibida uma mensagem
de alerta dependendo das condições:

temp maior 45: ALERTA!!! Perigo, calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA !!! Perigo de calor
úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp <0: Frio extremo
"""

import os
import sys
import logging
log = logging.Logger("alerta")

try: 
    temperatura = float(input("Qual é a temperatura atual?: "))
except ValueError:
    log.error("Temperatura inválida")
    sys.exit(1)

try: 
    umidade = float(input("Qual é a umidade atual?: "))
except ValueError:
    log.error("Umidade inválida")
    sys.exit(1)

if temperatura > 45:
    print("ALERTA!!! Perigo, calor extremo \U0001F975")
elif temperatura * 3 >= umidade:
    print("ALERTA !!! Perigo de calor úmido")
elif temperatura >= 10 and temperatura <= 30:
    print("Temperatura normal \U0001F60F")
elif temperatura >= 0 and temperatura <= 10:
    print("Temepratura fria \U0001F643")
elif temperatura < 0:
    print("Frio extremo \U0001F976")


