def loop_factorial(x: int) -> int:
    answer = 1
    for v in range(1, x + 1):
        answer *= v
    return answer


def recursive_factorial(x: int) -> int:
    if x == 1:
        return 1
    else:
        return x * recursive_factorial(x - 1)


if __name__ == "__main__":
    x = int(input("Enter an integer: "))
    print(loop_factorial(x))
    print(recursive_factorial(x))
