def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0] 
    return s


if __name__ == "__main__":
    s = "hello world!"
    print(reverse(s))