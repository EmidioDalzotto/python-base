"""
Confeccione um programa que tenha uma função chamada contador()
que vai receber três parâmetros: início, fim e passo, e realize 
a contagem.

O programa deve realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem a ser personalizada pelo usuário

"""
from time import sleep
import sys
import logging
log = logging.Logger("alerta")


def contador():
    print("-=" * 30)
    print("Contagem de 1 até 10 de 1 em 1")
    a = 1
    while a < 11:
        print(f" {a} ", end='', flush=True)
        sleep(0.5)
        a += 1
    print("FIM!")
    print("-=" * 30)
    print("Contagem de 10 até 0, de 2 em 2")
    b = 10
    while b > -1:
        print(f" {b} ", end='', flush=True)
        sleep(0.5)
        b -= 2
    print("FIM!")
    print("-=" * 30)
    print("Agora é a sua vez de personalizar a contagem!")
    
    try:
        c = int(input("Inicio: "))
        d = int(input("Fim: "))
        e = int(input("Passo: "))
    
        print(f"Contagem de {c} até {d} de {e} em {e}")
        if e == 0:
          e = 1
        if c < d:
          if e < 0:
            e = -e
            while c <= d:
                print(f" {c} ", end='', flush=True)
            sleep(0.5)
            c += e
        else:
            if e > 0:
                e = -e
            while c >= d:
                print(f" {c} ", end='',  flush=True)
                sleep(0.5)
            c += e
            print("FIM!")
    except ValueError:
        log.error("Utilize apenas números inteiros")
    sys.exit(1)


contador()