

import os
import sys

# LBYL - Look Before You Leap
# EAFP - Easy to Ask Forgiveness than Permission
# (É mais fácil pedir perdão do que permissão)


try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e))

try:
    names = open("names.txt").readlines()

except FileNotFoundError as e:
    print(f"[ERROR] {str(e)}.")
    sys.exit(1)
    #TODO:Usar retry
else:
    print("Sucesso!!")
finally:
    print("Execute isso sempre")

try:
    print(names[2])
except:
    print("[ERROR] Missing name in the list")
    sys.exit(1)
