import os


def lerProcessos(mesCorrente):
    NpuProcessos = []
    caminhoPasta = "auditoria"+mesCorrente
    listaDeArquivos = os.listdir(caminhoPasta)

    for relacao in listaDeArquivos:
        enderecoPasta = caminhoPasta+'\\'+str(relacao)
        file = open(enderecoPasta, "r")
        file.readline()
        linhasArquivo = file.readlines()
        for line in linhasArquivo:
            posicaoMarcador = line.find("-")
            NpuProcessos.append(
                line[posicaoMarcador-7:posicaoMarcador+18]+","+line[:posicaoMarcador+18])
    conjunto = set(NpuProcessos)
    nome_arquivo_saida = "relacaoAuditoria"+mesCorrente+".csv"
    arquivoRetorno = open(nome_arquivo_saida, "a")

    arquivoRetorno.write("NPU,CAMINHO")

    for linha in conjunto:
        # print(linha)
        if linha.count(',') >= 2:
            print(linha)
        else:
            arquivoRetorno.write(linha+"\n")


lerProcessos("Agosto")
