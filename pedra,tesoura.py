import random
import os
import time
vida = 0
perdeu = 0

def opções():
    global com
    opções = 'pedra','papel','tesoura'
    com = random.choice(opções)
    return com

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def hub():
    print ('-' * 70)
    print ('clássico "pedra,papel ou tesoura"\n'.upper())
    print("Regras:")
    print("\nQuem conseguir 5 pontos primeiro ganha;")
    print ("So pode usar (pedra,papel ou tesoura).")
    print("Obs.: O bot joga de forma 100% aleatóia; \ncaso ambos  jogarem o mesmo, o empate não gera ponto para ninguém")
    print ('-' * 70)
    print (f"Player = {vida} pontos")
    print (f"Bot = {perdeu} pontos")
    print ("-" * 30)

def player():
    while True:
        global ply
        ply = input("Escreva sua escolha\n").strip().lower()
        if ply == "tesoura" or ply == "pedra" or ply == "papel":
            return ply
            
        else:
            print ("Coloque algo válido")
            limpar_tela()

while True:
    hub()
    opções()
    if vida == 5:
        print ("Você ganhou do bot")
        time.sleep(5)
        break
    elif perdeu == 5:
        print ("O bot ganhou de você")
        time.sleep(5)
        break
    player()
    if ply == "papel" and com == "pedra" \
    or ply == "pedra" and com == "tesoura" \
    or ply == "tesoura" and com == "papel":
        print ("Você marcou 1 ponto")
        vida += 1
        time.sleep(2)
        limpar_tela()
    else:
        print ("O bot marcou 1 ponto")
        perdeu += 1
        time.sleep(2)
        limpar_tela()
