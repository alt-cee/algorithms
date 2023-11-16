def is_palindrome(s):
    """
    y
    aya
    kayak
    """
    if len(s) <= 0:
        return True
    else:
        equal_ends = s[0] == s[-1]
        return is_palindrome(s[1:-1]) and equal_ends



if __name__ == "__main__":
    s = "kayak"
    print(is_palindrome(s))