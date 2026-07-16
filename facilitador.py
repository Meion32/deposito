C1 = float(input("Qual a corrente 1\n").strip())
C2 = float(input("Qual a corrente 2\n").strip())
C3 = float(input("Qual a corrente 3\n").strip())
c1 = C1 / 1000
c2 = C2 / 1000
c3 = C3 / 1000
def Tensão(Resistor):
        global t1, t2, t3, tf12, tf13, tf23
        t1 = Resistor * c1
        t2 = Resistor * c2
        t3 = Resistor * c3
        tf12 = Resistor * front12
        tf13 = Resistor * front13
        tf23 = Resistor * front23
def cal_front(nome,A,B):
    while True:
        resposta = input (f"A {nome} esta invertida?(sim/não)\n").strip().lower()
        if resposta == "sim":
            return A - B
        elif resposta == "não":
            return A + B
        else:
            print ("Coloque apenas sim ou não\n")
def fronteiras(c1,c2,c3):
    global front12, front13, front23
    front12 = cal_front("1/2", c1, c2)
    front13 = cal_front("1/3", c1, c3)
    front23 = cal_front("1/2", c2, c3)   
fronteiras(c1,c2,c3)
while True:
    conta = input("Você quer descobrir tensão,potência ou corrente?\n").strip().lower()
    if conta == "tensão".lower():
        while True:
            Resistor = int(input("Qual o resistor para conta\n").strip())
            Tensão(Resistor)
            cal = input("Qual camada você quer achar a tensão?\n").strip().lower()
            
            if cal == "I1".lower():
                print (f"Tensão = {t1:.3f} V")
            
            elif cal == "I2".lower():
                print (f"Tensão = {t2:.3f} V")
            
            elif cal == "I3".lower():
                print (f"Tensão = {t3:.3f} V")

            elif cal == "fronteira".lower():
                fronteira = input ("Qual fronteira?")
                
                if fronteira == "fronteira12".lower():
                    print (f"Tensão = {tf12:.3f} V")
                
                elif fronteira == "fronteira13".lower():
                    print (f"Tensão = {tf13:.3f} V")
                
                elif fronteira == "fronteira23".lower():
                    print(f"Tensão = {tf23:.3f} V")
            
            elif cal == "trocar".lower():
                break
        
    elif conta == "potencia".lower():
        
        while True:
            Resistor = int(input("Qual o resistor para conta\n").strip())
            Tensão(Resistor)
            escolha = input ("Você quer saber de qual camada??\n").strip().lower()
            
            if escolha == "I1":
                print (f"Potência = {t1 * c1:.3f} W")
                
            elif escolha == "I2":
                print (f"Potência = {t2 * c2:.3f} W")

            elif escolha == "I3".lower():
                print (f"Potência = {t3 * c3:.3f} W")
            
            elif escolha == "fronteira":
                fronteira = input("Qual fronteira?\n")
                
                if fronteira == "fronteira12":
                    print (f"Potencia = {tf12 * front12:.3f} W")
                
                elif fronteira == "fronteira13":
                    print (f"Potência = {tf13 * front13:.3f} W")
                
                elif fronteira == "fronteira23":
                    print (f"Potência = {tf23 * front23:.3f} W")
            
            elif escolha == "trocar":
                break
    elif conta == "corrente":
            Resistor = int(input("Qual o resistor para conta\n").strip())
            Tensão(Resistor)
            escolha = input ("Você quer saber de qual camada??\n").strip().lower()
            
            if escolha == "I1":
                print (f"Corrente = {C1} W")
                
            elif escolha == "I2":
                print (f"Corrente = {C2} W")

            elif escolha == "I3":
                print (f"Corrente = {C3} W")
            
            elif escolha == "fronteira":
                fronteira = input("Qual fronteira?\n")

                if fronteira == "fronteira12":
                    print (f"Corrente = {front12:.3f} W")
                
                elif fronteira == "fronteira13":
                    print (f"Corrente = {front13:.3f} W")
                
                elif fronteira == "fronteira23":
                    print (f"Corrente = {front23:.3f} W")
    else:
        break