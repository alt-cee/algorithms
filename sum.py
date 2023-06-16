def sum(a: list) -> int:
    if len(a) == 1:
        return a[0]
    else:
        return a[0] + sum(a[1:])
    

if __name__ == "__main__":
    print(sum([1, 1, 1, 1, 1, 5]))