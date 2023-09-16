# from bubble.bubbleSort import bubble_sort
from algoritmos.bubble.bubbleSort import bubble_sort
from algoritmos.insertion.insertionSort import insertion_sort
from algoritmos.merge.mergeSort import merge_sort
from algoritmos.quick.quickSort import quick_sort
from algoritmos.selection.selectionSort import selection_sort

import os



def dicionarios():
    dict_tipo_lista = {
        'o': {'nome':'Ordenada' ,'tipo': 'lista_o'}, 
        'no': {'nome':'Não Ordenada' ,'tipo': 'lista_no'}
    }

    dict_algoritmos = {
        'a': {'nome':'Insertion sort', 'alg': insertion_sort, 'output': 'insertion'},
        'b': {'nome':'Selection Sort', 'alg': selection_sort, 'output': 'selection'},
        'c': {'nome':'Bubble sort', 'alg': bubble_sort, 'output': 'bubble'},
        'd': {'nome':'Merge Sort', 'alg': merge_sort, 'output': 'merge'},
        'e': {'nome':'Quicksort', 'alg': quick_sort, 'output': 'quick'},
    }
    
    dict_instancias = {
        1: '100', 
        2: '200', 
        3: '1000', 
        4: '2000', 
        5: '5000', 
        6: '10000', 
        7: '50000', 
        8: '100000', 
        9: '500000', 
        10: '1000000', 
        11: '5000000', 
        12: '10000000', 
        13: '100000000'
    }

    dicionarios = {
        't': dict_tipo_lista,
        'a': dict_algoritmos,
        'i': dict_instancias
    }

    return dicionarios