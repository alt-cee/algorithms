def count(a: list) -> int:
    if a == []:
        return 0
    else:
        return 1 + count(a[1:])
    

if __name__ == "__main__":
    print(count([1, 1, 1, 1, 1, 5]))