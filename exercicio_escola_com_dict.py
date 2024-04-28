#!/usr/bin/env python
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que
frequentam cada uma das atividades.
"""

__version__ = "0.1.0"

#Dados

salas = {
    "Sala 1": ["Erik", "Maia", "Gustavo", "Sofia", "Joana"],
    "Sala 2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

atividades = {
    "Inglês" : ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música" : ["Erik", "Carlos", "Maria"],
    "Dança" : ["Gustavo", "Sofia", "Joana", "Antonio"]
}

#Listar alunos em cada atividade por sala

for nome_atividade, alunos_atividade in atividades.items():
    
    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    # Verificar alunos presentes em cada sala para a atividade atual

    atividade_sala1 = [aluno for aluno in alunos_atividade if aluno in salas["Sala 1"]]
    atividade_sala2 = [aluno for aluno in alunos_atividade if aluno in salas["Sala 2"]]

          
    print(f"A {nome_atividade} Sala 1", atividade_sala1)
    print(f"A {nome_atividade} Sala 2", atividade_sala2)
    
    print()
    print("#" * 40)


