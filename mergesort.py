from math import log2

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
            a.append(array[k])  # appending a list cf. appending an int
    else:
        for k in range(i, m):
            a.append(array[k])
    
    for i in range(len(array)):
        array[i] = a[i]
            

def iMergeSort(array, m):
    for i in [2 ** x for x in range(0, int(log2(m)) + 1)]:  # create a relative step in sequence
        for j in range(int(m / i)):
            merge(array, j * 2, j * 2 + i, j * 2 + i - 1, j * 2 + 2 * i)
    return array
    


if __name__ == "__main__":
    array = [10, 5, 2, 6, 4, 11, 1]
    print(iMergeSort(array, len(array)))