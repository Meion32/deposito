import os 
import shutil

caminho = (r"C:\Users\konke\OneDrive\Área de Trabalho\bonricio")
processo = os.listdir(caminho)
for item in processo:
    nome , extensão = os.path.splitext(item)
    if extensão == "":
        continue
    nome_p = extensão[1:]
    caminho_pastaN = os.path.join(caminho, nome_p)
    if not os.path.exists(caminho_pastaN):
        os.mkdir(caminho_pastaN)
    origem = os.path.join(caminho,item)
    destino = os.path.join(caminho_pastaN,item)
    shutil.move(origem,destino)
