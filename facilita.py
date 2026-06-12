 C1 = float(input("Qual a corrente 1\n"))
C2 = float(input("Qual a corrente 2\n"))
C3 = float(input("Qual a corrente 3\n"))
c1 = C1 / 1000
c2 = C2 / 1000
c3 = C3 / 1000
front12 = c1 + c2
front13 = c1 + c3
front23 = c2 + c3
while True:
    conta = input("Você quer descobrir tensão ou potencia?\n").strip().lower()
    if conta == "tensão".lower():
        while True:
            Resistor = int(input("Qual o resistor para conta\n").strip())
            t1 = Resistor * c1
            t2 = Resistor * c2
            t3 = Resistor * c3
            tf12 = Resistor * front12
            tf13 = Resistor * front13
            tf23 = Resistor * front23
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
            t1 = Resistor * c1
            t2 = Resistor * c2
            t3 = Resistor * c3
            tf12 = Resistor * front12
            tf13 = Resistor * front13
            tf23 = Resistor * front23
            escolha = input ("Você quer saber de qual camada??\n").strip().lower()
            
            if escolha == "I1".lower():
                print (f"Potência = {t1 * c1:.3f} W")
                
            elif escolha == "I2".lower():
                print (f"Potência = {t2 * c2:.3f} W")

            elif escolha == "I3".lower():
                print (f"Potência = {t3 * c3:.3f} W")
            
            elif escolha == "fronteira".lower():
                fronteira = input("Qual fronteira?\n")
                
                if fronteira == "fronteira12".lower():
                    print (f"Potencia = {tf12 * front12:.3f} W")
                
                elif fronteira == "fronteira13".lower():
                    print (f"Potência = {tf13 * front13:.3f} W")
                
                elif fronteira == "fronteira23".lower():
                    print (f"Potência = {tf23 * front23:.3f} W")
            
            elif escolha == "trocar".lower():
                break
    else:
        break