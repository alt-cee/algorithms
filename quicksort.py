def quickSort1(array: list):

    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x <= pivot]
        right = [x for x in array[1:] if x > pivot]
        return quickSort1(left) + [pivot] + quickSort1(right)
    

def swap(array: list, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return None


def partition(array:list, l:int, h: int):
    """
    Sorts values into less than and greater than the pivot value in place and
    returns the sorted location of the pivot (first element) in the array.
    """
    if l == h:
        return l
    
    else:
        pivot = array[l]
        i = l + 1
        j = h

        while i < j:
            while array[i] <= pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            swap(array, i, j)
            i += 1
            j -= 1
            array.insert(j, array.pop(l))
        
        return j


def quickSort2(array:list, l:int, h: int):
    
    

if __name__ == "__main__":
    array = [10, 5, 2, 6, 4, 11, 1]
    print("array: ", array)
    # print("quickSort1: ", quickSort1(array))
    print("partition: ", partition(array, 0, len(array) - 1))
    # print("quickSort2: ", quickSort2(array))