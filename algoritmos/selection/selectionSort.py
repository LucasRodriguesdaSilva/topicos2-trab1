def selection_sort(arr):
    for i in range(len(arr)):
        indice_minimo = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j

        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

    return True