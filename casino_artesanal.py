import os
import time
import random
hakari = "7","🍒","🔔","🍏","🎲","🏅"
dindin = 25
def hub ():
    print ("-" * 70)
    print ("🎰Esse jogo é totalmente ficticio e inspirado em caça niqueis🎰") 
    print ("\n Seu objetivo é conseguir R$ 1000")
    print ("Você inicia com R$ 25 e gasta R$1 a cada giro")
    print ("Que a sorte esteja convosco")
def tabela ():

    print (" 7 7 7 = R$ 700")
    print ("🍒🍒🍒 = R$ 300")
    print ("🔔🔔🔔 = R$ 200")
    print ("🍏🍏🍏 = R$ 500")
    print ("🎲🎲🎲 = R$ 100")
    print ("🏅🏅🏅 = R$ 127")
    print ("-" * 70)
def sorte(cx_1,cx_2,cx_3):
    global dindin
    if cx_1 == "7" and cx_2 == cx_1 and cx_3 == cx_1:
        print ("JackPot")
        dindin += 700
        time.sleep(1)
    elif cx_1 == "🍒" and cx_2 == cx_1 and cx_3 == cx_1:
        print ("JackPot")
        dindin += 300
        time.sleep(1)
    elif cx_1 == "🔔" and cx_2 == cx_1 and cx_3 == cx_1:
        print ("JackPot")
        dindin += 200
        time.sleep(1)
    elif cx_1 == "🍏" and cx_2 == cx_1 and cx_3 == cx_1:
        print ("JackPot")
        dindin += 500
        time.sleep(1)
    elif cx_1 == "🎲" and cx_2 == cx_1 and cx_3 == cx_1:
        print ("JackPot")
        dindin += 100
        time.sleep(1)
    elif cx_1 == "🏅" and cx_2 == cx_1 and cx_3 == cx_1:
        print ("JackPot")
        dindin += 127
        time.sleep(1)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

hub()
tabela()
try:
    giro = input("Você quer jogar?(s/n)\n").strip().lower()

except NameError:
    print ("Coloque algo válido")
match giro:
    case "s":
        while True:    
            
            cx_1 = random.choice(hakari)
            cx_2 = random.choice(hakari)
            cx_3 = random.choice(hakari)
            
            roletar = input (f"Clique 'ENTER' para girar \n Saldo: {dindin}").strip()
            
            if dindin == 0 or dindin < 1:
                print ("🩻🩻🩻Você chegou a falência🩻🩻🩻")
                time.sleep(2)
                break
            
            elif dindin >= 1000:
                print ("🎉🎉🎉Você pagou suas dividas🎉🎉🎉")
                time.sleep(2)
                break
            
            if roletar == "":
                limpar_tela()
                hub()
                tabela()
                print ("-" * 10)
                print (cx_1, cx_2,cx_3)
                sorte(cx_1,cx_2,cx_3)
                print ("-" * 10)
                dindin -= 1
                time.sleep(0.25)
    case "n":
        print ("Volte quando estiver pronto")
    case _:
        print ("coloque apenas 's' ou 'n'")
