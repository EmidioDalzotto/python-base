"""
Faça um programa que tenha uma função chamada maior(), a qual
recebe vários parâmetros com valores inteiroes, os analisa e diz
qual é o maior.

"""
#minha resolução

from time import sleep
import sys
import logging

log = logging.Logger("alerta")

def maior (* x):
    try:
        print("-=" * 30)
        print("Analisando os valores passados...")
        print(f"Os valores informados foram {x},sendo ao todo {len(x)} números") 
       
        print(f"O maior valor informado foi {max(x)}.")
    except TypeError:
        log.error("por favor, informe apenas números.")
    except ValueError:
        log.error("Não foi informado nenhum valor!")


maior(5, 2, 3,)
maior(10, 20, 30, 99, 135)
maior(0)
maior()

#resolução do professor

def maior_aula(* núm):
    cont = maior_aula = 0
    print("-=" * 30)
    print('\nAnalisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior_aula = valor
        else:
            if valor > maior_aula:
                maior_aula = valor
        cont +=1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior_aula}.')


maior_aula(5, 2, 3,)
maior_aula(10, 20, 30, 99, 135)
maior_aula(0)
maior_aula()