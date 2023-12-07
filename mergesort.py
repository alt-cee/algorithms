from math import log2

def merge(array: list, l, m, h) -> None:
    a = []
    i = l
    j = m + 1

    while (i <= m and j <= h):
        if array[i] <= array[j]:
            a.append(array[i])
            i += 1
        else:
            a.append(array[j])
            j += 1
    
    if i > m:
        for k in range(j, h + 1):
            a.append(array[k])  # appending a list cf. appending an int
    else:
        for k in range(i, m + 1):
            a.append(array[k])
    
    for q in range(len(a)):
        array[l + q] = a[q]
            

def iMergeSort(array, m):
    p = 2
    while p <= m:
        i = 0
        while i + p <= m:
            low = i
            high = i + p - 1
            mid = (high + low) // 2
            merge(array, low, mid, high)
            i += p
        p *= 2
    return array


def rMergeSort(array, l, h):
    pass
    


if __name__ == "__main__":
    array = [10, 5, 2, 6, 4, 11, 1, 3]
    # test merge
    # x = [1, 3, 2, 4]
    # merge(x, 0, 1, 3)
    # print(x)

    # test iMergeSort
    print(iMergeSort(array, len(array)))
    print(rMergeSort(array, 0, len(array)))