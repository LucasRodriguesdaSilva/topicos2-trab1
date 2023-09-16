def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        troca = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                troca = True
        
        if not troca:
            break

    return True

