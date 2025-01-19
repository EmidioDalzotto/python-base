"""

Faça um programa em python que abra e reproduza o áudio de um arquivo MP3

"""

#bash pip install pygame

import pygame
import os


# Inicializando o mixer do pygame
pygame.mixer.init()

music = input("Informe o nome do arquivo MP3 que deseja ouvir: ")

if not os.path.isfile(music):
    print(f"Arquivo {music} não encontrado.")
else:
    pygame.mixer.music.load(music)
    
    pygame.mixer.music.play()

    print(f"Tocando {music}...")
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

