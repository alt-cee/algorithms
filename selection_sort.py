def find_smallest(a: list) -> int:
    """
    Finds the index of the smallest value in the array.
    """
    min = a[0] # need to keep track of the min value
    index = 0
    for i in range(1, len(a)):
        if a[i] < min:
            min = a[i]
            index = i
    return index

def selection_sort(a: list) -> list:
    """
    Sorts the items in the array 'a' in order from smallest to largest.
    """
    sorted_a = []
    for i in range(len(a)):
        index_smallest = find_smallest(a)
        smallest = a.pop(index_smallest) # deleting from an array, modifying the input array
        sorted_a.append(smallest)  # inserting into an array
    return sorted_a

if __name__ == "__main__":
    print(selection_sort([-1, -5, 7, 2, 9]))