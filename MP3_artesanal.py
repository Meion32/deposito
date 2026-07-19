import os 
import pathlib
import time
import threading
import json
import pygame
#inico do pygame
pygame.init()
pygame.mixer.init()

#busca pela pasta de musicas e criação de playlist
pasta_musicas = "musicas"
playlist = []
for arquivo in os.listdir(pasta_musicas):
    if arquivo.endswith(".mp3") or arquivo.endswith(".wav"):
        playlist.append(
            os.path.join (pasta_musicas,arquivo) 
        )
print (playlist)

#Escolher qual musica tocar 
while True:
    try:
        escolha = int(input("Qual musica você quer tocar?"))
        break
    except ValueError:
        print ("Coloque apenas númer inteiros como resposta")

#Validando escolha e rodando a musica
if (0 < escolha) and (escolha <= len(playlist)):
    atual = playlist[escolha - 1]
    print("Carregando:", atual)
    pygame.mixer.music.load(atual)
    print("Música carregada!")
    pygame.mixer.music.play()
    print("Comando play enviado!")
    input ("preciso ENTER para acabar a musica")
else:
    print (f"Coloque um número entre 1 e {len(playlist)}") 