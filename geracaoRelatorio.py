import os

# path = "C:\\Users\\edils\\OneDrive\\Documentos\\Projeto\\arquivosMaio"
MES = "Julho"
PATH_RELATIVO = "auditoria"+MES
lista = os.listdir(PATH_RELATIVO)
processoNPU = []
ARQUIVO_SAIDA = "resultado"+MES+"Junho.csv"
TIPO_ESCRITA = "a"


def lerPasta(pasta):

    return pasta


def abrir(CAMINHO):
    return open(CAMINHO, "r")


for a in lista:
    caminho = PATH_RELATIVO+'\\'+str(a)
    f = abrir(caminho)
    f.readline()
    listaDoArquivo = f.readlines()
    for l in listaDoArquivo:
        marcador = l.find("-")
        processoNPU.append(l[marcador-7:marcador+18]+","+l[:marcador+18])
      #  processoNPU.append(l[marcador-7:marcador+18])

NPUs = set(processoNPU)
r = open(ARQUIVO_SAIDA, TIPO_ESCRITA)
for p in NPUs:
    r.write(p+"\n")