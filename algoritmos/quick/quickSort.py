def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivo = arr[len(arr) // 2]  # Escolhe o elemento do meio como pivô
    esquerda = [x for x in arr if x < pivo]
    meio = [x for x in arr if x == pivo]
    direita = [x for x in arr if x > pivo]

    return quick_sort(esquerda) + meio + quick_sort(direita)
