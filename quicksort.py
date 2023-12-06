def quicksort(array: list):
    if len(array) < 2:
        return array
    # elif len(array) == 2:
    #     if array[0] < array[1]:
    #         return array
    #     else:
    #         return [array[1], array[0]]
    else:
        pivot = array.pop()
        left = []
        right = []
        for i in array:
            if i >= pivot:
                right.append(i)
            else:
                left.append(i)
        return quicksort(left) + [pivot] + quicksort(right)

if __name__ == "__main__":
    array = [100, 2, 1, 870, 0, 3, -5]
    print(quicksort(array))