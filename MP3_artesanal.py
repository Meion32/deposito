import os 
import pathlib
import time
import threading
import json
import pygame
pygame.init()
pygame.mixer.init()


pasta_musicas = "musicas"
playlist = []
for arquivo in os.listdir(pasta_musicas):
    if arquivo.endswith(".mp3") or arquivo.endswith(".wav"):
        playlist.append(
            os.path.join (pasta_musicas,arquivo) 
        )
        print (f"-- {arquivo}")

print (playlist)
while True:
    try:
        escolha = int(input("Qual musica você quer tocar?"))
        break
    except ValueError:
        print ("Coloque apenas númer inteiros como resposta")

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

#Opção de cores
cores = {
    "branca": (255,255,255),
    "preto": (0,0,0)
}


#Configuração de tamanho, junto com titulo
tamanho_tela = (600,600)

tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("MP3_Artesanal")

teste = pygame.Rect(100,500,15,15)

tela.fill(cores["preto"])
