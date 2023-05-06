def countdown(x: int) -> None:
    print(x, "...")
    if x == 1:
        return
    else:
        return countdown(x - 1)
    

if __name__ == "__main__":
    x = int(input("Enter an integer: "))
    countdown(x)