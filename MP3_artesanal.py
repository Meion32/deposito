import os 
import pathlib
import time
import threading
import json
import pygame
#inico do pygame
pygame.init()
pygame.mixer.init()

def hub():
    print ("-" * 50)
    print ("1) Pausar")
    print ("2) Continuar")
    print ("3) Parar")
    print ("4) Escolher música")
    print ("5) Sair")
    print ("-" * 50)
#busca pela pasta de musicas e criação de playlist
pasta_musicas = "musicas"
playlist = []
for arquivo in os.listdir(pasta_musicas):
    if arquivo.endswith(".mp3") or arquivo.endswith(".wav"):
        playlist.append(
            os.path.join (pasta_musicas,arquivo) 
        )
#Escolher qual musica tocar 
def escolher(playlist):        
    total = len(playlist)
    n = int(0)
    while True:
        while True:
            try:
                nome = os.path.basename(playlist[n])
                break
            except IndexError:
                n -= n
        print (f"{n + 1}/{total}")
        print (nome)
        seleção = input("< o >\n").strip().lower()
        match seleção:
            case "o":
                return n
            case ">":
                n += 1
            case "<":
                if n == 0:
                    print ("Você ja esta na primeira musica")    
                else:
                    n-= 1
def tocar(indice):
    toca = playlist[indice]
    pygame.mixer.music.stop()
    print("Carregando:", os.path.basename(toca))
    pygame.mixer.music.load(toca)
    print("Música carregada!")
    pygame.mixer.music.play()
    print("Comando play enviado!")
while True:
    hub()
    while True:
        try:
            player = int(input("\n"))
            break
        except ValueError:
            print ("Escolha apenas um número válido")
    match player:
        case 1:
            pygame.mixer.music.pause()
        case 2:
            pygame.mixer.music.unpause()
        case 3:
            pygame.mixer.music.stop()
        case 4:
            indice = escolher(playlist)
            tocar(indice)
        case 5:
            print ("Volte quando necessario")
            time.sleep(1)
            break