def find_smallest(a: list) -> int:
    """
    Finds the index of the smallest value in the array.

    Args:
        a (list): The array 'a' to search for the smallest value.

    Returns:
        int: The index of the smallest value in the array 'a'.
    """
    min = a[0]
    index = 0
    for i in range(1, len(a)):
        if a[i] < min:
            min = a[i]
            index = i
    return index


def selection_sort(a: list) -> list:
    """
    Sorts a list of comparable items in the array 'a' in order from smallest 
    to largest using the selection sort algorithm.

    Selection sort works by iteratively finding the minimum of the input array 
    'a' and adding it to the end of a new list. 

    Args:
        a (list): An array of items to sort.

    Returns:
        list: A sorted array.
    """
    sorted_a = []
    for i in range(len(a)):
        index_smallest = find_smallest(a)
        smallest = a.pop(index_smallest)
        sorted_a.append(smallest)
    return sorted_a


if __name__ == "__main__":
    print(selection_sort([-1, -5, 7, 2, 9]))