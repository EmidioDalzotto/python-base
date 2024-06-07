"""Calculadora

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `infixcalc.log`
"""

__version__ = "0.1.0"

import os
import sys
import logging

from datetime import datetime

#configuração do logging
log_filepath = os.path.join(os.curdir, "infixcalc.log")
logging.basicConfig(
    filename = log_filepath,
    level = logging.DEBUG,
    format = '%(asctime)s - %(user)s - %(levelname)s - %(message)s'
)


arguments = sys.argv[1:]


#Validacao
if not arguments:
    operation = input("operação:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
    
try:
    operation, * nums = arguments
except Exception as e:
    print(f"[ERROR]{str(e)}")
    print("Número de argumentos inválidos")
    print("ex: `sum 5 5`")
    sys.exit(1)



valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO usar exceptions + while
    if not num.replace(".", "").isdigit():
      print(f"Número inválido {num}")
      sys.exit(1)
    if"." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

try:
    n1, n2 = validated_nums
except ValueError as e:
    print(str(e))
    sys.exit(1)

# TODO: Usar dicionario de funcoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2


path= os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")
except PermissionError as e:
    logging.error("Erro ao desempacotar números", exc_info = True, extra = {'user': os.getenv('USER', 'anonymous')})
    print(str(e))
    sys.exit(1)

# print(f"{operation}, {n1}, {n2} = {restul}", file=open(filename, "a"))

print(f"O resultado é {result}")