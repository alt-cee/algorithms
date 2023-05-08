def max(a: list) -> int:
    if len(a) == 1:
        return a[0]
    else:
        if a[0] > max(a[1:]):
            return a[0]
        else:
            return max(a[1:])


if __name__ == "__main__":
    print(max([9, 100, 2, 3, 1000, -1]))