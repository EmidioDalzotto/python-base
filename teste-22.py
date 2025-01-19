"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

- o nome com todas as letras maiúsculas;
- o nome com todas as letras minúsculas;
- quantas letras ao todo (sem considerar os espaços);
- quantas letras tem o primeiro nome.

"""

nome = str(input("Qual é o seu nome? ")).strip()
nome_maiusculas = nome.upper()
nome_minusculas = nome.lower()
letras_total = len([char for char in nome if char != " "])
pri_nome = nome.split()[0]
letras_prim_nome = len(pri_nome)
print(f"seu nome com todas as letras em maísculas fica {nome_maiusculas}"
      f", já com todas as letras minúsculas fica {nome_minusculas},"
       f" são ao todo {letras_total} letras, sendo destas"
        f" {letras_prim_nome} a quantia de letras do primeiro nome." )