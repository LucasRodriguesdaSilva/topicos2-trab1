from utils.dicionarios_utilizados import dicionarios
import utils.arguments as arguments
import utils.output_info as info
from utils.ler_arquivos import ler_arquivo 
from utils.salvar_dados import salvarInformacoes

import os 
import tracemalloc
import time 
import colorama
from colorama import Fore, Style


def __get_caminho_absoluto():
    return os.path.dirname(os.path.abspath(__file__)) 

def __get_caminho_arquivo(tipo, instancia):
    nomeInstancia = f'{instancia}.txt'
    dir_raiz = __get_caminho_absoluto()
    caminhoArquivo = os.path.join('utils', tipo)
    caminhoCompleto = os.path.join(dir_raiz, caminhoArquivo, nomeInstancia)

    return caminhoCompleto


def __get_caminho_output(pasta, nomeInstancia):
    dir_raiz = __get_caminho_absoluto()
    saida = os.path.join(dir_raiz,'output',pasta,nomeInstancia)
    return saida


def __medicoes(algoritmo, *args):
    tracemalloc.start()
    inicio = time.time()
    r = algoritmo(*args)
    fim = time.time()
    tempo_execucao = fim - inicio
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    current = current / 10**6
    peak = peak / 10**6

    return tempo_execucao, current, peak, r

def main():
    colorama.init()
    info.mensagemInicial()

    
    utilsDict = dicionarios()

    opts = arguments.arguments_main()

    propriedadesAlg = utilsDict['a'][opts.a]
    instancia = utilsDict['i'][opts.i]
    tipoLista = utilsDict['t']['no']

    numLoops = opts.n_loop

    info.mensagemInstanciaInit()
    caminhoInstancia = __get_caminho_arquivo(tipoLista['tipo'], instancia)
    conteudo = ler_arquivo(caminhoInstancia)
    info.mensagemInstanciaFim()

    info.imprimirInfoPadrao(propriedadesAlg['nome'], instancia, tipoLista['nome'], numLoops)

    saida = __get_caminho_output(propriedadesAlg['output'],instancia)

    resultados = {}

    for i in range(numLoops):
        print(f"Iteração {i + 1} de {numLoops}", end="\r")  # \r para voltar ao início da linha

        tempo_execucao, uso_memoria_atual, uso_memoria_pico, r = __medicoes(propriedadesAlg['alg'],conteudo)

        resultados[i] = {}

        resultados[i]['Tempo de Execucao'] = tempo_execucao
        resultados[i]['Memoria Atual'] = uso_memoria_atual
        resultados[i]['Memoria Pico'] = uso_memoria_pico

        time.sleep(0.1)
        print(" " * len(f"Iteração {i + 1} de {numLoops}"), end="\r")  # Limpar a linha

    salvarInformacoes(resultados, saida)
    print(Fore.GREEN + "Concluído!" + Style.RESET_ALL)  # Imprimir concluído em verde
    




        



if __name__ == "__main__":
    main()