def binary_search(k: int, a: list) -> int:
    """
    Searches for an integer in a sorted array using binary search. Will return 
    only one index for the integer k if it occurs more than once in the array
    a.

    Args:
        k (int): The integer to search for in the array a.
        a (list): A sorted list of integers possibly containing k.
    
    Returns:
        int: The index of the integer k in the array a if found
        None: If the integer k is not found in the array a
    """
    start_pointer = 0
    end_pointer = len(a) - 1 
    while start_pointer <= end_pointer:  # condition based on pointer location
        mid_pointer = (start_pointer + end_pointer) // 2
        guess = a[mid_pointer]
        if guess == k:
            return mid_pointer
        elif guess < k:
            start_pointer = mid_pointer + 1  # slide search window to the right
        else:
            end_pointer = mid_pointer - 1  # slide search window to the left
    return None


def main():
    k = int(input("Enter integer to search for: "))
    print(binary_search(k, [-1, 2, 5, 6, 7, 7, 9, 10]))

if __name__=="__main__":
    main()
    