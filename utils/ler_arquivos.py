import os 

def ler_arquivo(caminho):

    with open(caminho, 'r') as arquivo:
        conteudo = arquivo.read()
    
    linhas = conteudo.split('\n')
    vetor = []

    for linha in linhas:
        numeros = linha.split(',')
        for numero_str in numeros:
            if numero_str.strip():
                numero = int(numero_str)
                vetor.append(numero)
    
    return vetor