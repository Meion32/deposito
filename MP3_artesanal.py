import os 
import pathlib
import time
import threading
import json
import pygame

#Opção de cores
cores = {
    "branca": (255,255,255),
    "preto": (0,0,0)
}


#Iniciar a tela
pygame.init()

#Configuração de tamanho, junto com titulo
tamanho_tela = (600,600)
while True:
    tela = pygame.display.set_mode(tamanho_tela)
    pygame.display.set_caption("MP3_Artesanal")

    teste = pygame.Rect(100,500,15,15)

    tela.fill(cores["preto"])
