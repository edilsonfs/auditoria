import os

#path = "C:\\Users\\edils\\OneDrive\\Documentos\\Projeto\\arquivos"
PATH_RELATIVO = "arquivos"
lista = os.listdir(PATH_RELATIVO)
processoNPU = []


def abrir(CAMINHO):
    return open(CAMINHO, "r")


for a in lista:
    CAMINHO = PATH_RELATIVO+'\\'+str(a)
    f = abrir(CAMINHO)
    f.readline()
    listaDoArquivo = f.readlines()
    for l in listaDoArquivo:
        marcador = l.find("-")
        processoNPU.append(l[marcador-7:marcador+18])
    NPUs = set(processoNPU)
    r = open("resultado.txt", "a")
    for p in NPUs:
        r.write(p+"\n")
        print(p)
