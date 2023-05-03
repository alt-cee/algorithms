def binary_search(k: int, a: list) -> int:
    start_pointer = 0
    end_pointer = len(a) - 1 
    mid_pointer = (start_pointer + end_pointer) // 2
    v = a[mid_pointer]
    while v != k:
        if v > k:
            end_pointer = mid_pointer
        else:
            start_pointer = mid_pointer
        mid_pointer = (start_pointer + end_pointer) // 2
        v = a[mid_pointer]
    return mid_pointer


def main():
    print(binary_search(10, [-1, 2, 5, 6, 7, 9, 10]))

if __name__=="__main__":
    main()
    