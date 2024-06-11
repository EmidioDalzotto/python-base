"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras
e imprime cada uma das palavras com suas vogais duplicadas.

"""
import sys
import os
import logging

log = logging.Logger("alerta")

try:
   palavra = str(input("Digite uma palavra ou enter para sair: ")).lower()
except ValueError:
   log.error("Digite apenas palavras com letras")
   sys.exit(1)

vogais = ("aeiouAEIOU")

nova_palavra = ""

for caractere in palavra:
    if caractere in vogais:
       nova_palavra += caractere * 2
    else:
       nova_palavra += caractere

print(nova_palavra)
    

words = []
while True:
   word = input("Digite uma palavra (ou enter para sair): ").strip()
   if not word: #condiçaõ de parada
       break
   
   final_word = ""
   for letter in word:
        #TODO: Remover acentuação usando função
        if letter.lower() in "aeiou":
            final_word += letter * 2
        else:
            final_word += letter
            
      # if ternario
      #  final_word += letter * 2 if letter.lower() in "aeiouãêéáí"else letter)

words.append(final_word)

print(*words, sep="\n")
