######## Heap Sort

List = [2, 8, 5, 3, 9, 1]
print(List)


def swap(List, i, j):
    List[i], List[j] = List[j], List[i]


def heapify(List, i, Upper):
    while True:
        L = 2 * i + 1
        R = 2 * i + 2
        if max(L, R) < Upper:
            if List[i] > max(List[L], List[R]):
                break
            elif List[L] > List[R]:
                swap(List, i, L)
                i = L
            else:
                swap(List, i, R)
                i = R
        elif L < Upper:
            if List[L] > List[i]:
                swap(List, i, L)
                i = L
            else:
                break
        elif R < Upper:
            if List[R] > List[i]:
                swap(List, i, R)
                i = R
        else:
            break


def heapsort(List):
    n = len(List)
    for i in range((n - 2) // 2, -1, -1):
        heapify(List, i, n)
    for i in range(n - 1, 0, -1):
        swap(List, 0, i)
        heapify(List, 0, i)


heapsort(List)
print("your sorted List:")
print(List)
