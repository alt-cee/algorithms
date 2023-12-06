def merge(array: list, i:int, j:int, m:int, n:int) -> None:
    a = []

    while (i < m and j < n):
        if array[i] <= array[j]:
            a.append(array[i])
            i += 1
        else:
            a.append(array[j])
            j += 1
    
    if i >= m:
        for k in range(j, n):
            a.append(array[k])
    else:
        for k in range(i, m):
            a.append(array[k])
    
    for i in range(len(array)):
        array[i] = a[i]
            


def mergeSort():
    pass


if __name__ == "__main__":
    array = [10, 5, 2, 6, 4, 11, 1]
    x = [1, 3, 5, 2, 4, 6]
    merge(x, 0, 3, 3, 6)
    print(x)
    # print(mergeSort(array))