def factorial(x: int) -> int:
    answer = 1
    for v in range(1, x + 1):
        answer *= v
    return answer


if __name__ == "__main__":
    x = int(input("Enter an integer: "))
    print(factorial(x))