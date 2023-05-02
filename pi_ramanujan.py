import math 

def pi(k: int) -> float:
    """
    Calculates an approximation of pi using the Ramanujan series. 

    Args:
        k (int): The number of terms of the Ramanujan series to use in the
        approximation. 
    
    Returns:
        float: An approximation of pi based on the first k terms of the series.
    """
    a = (2 * math.sqrt(2)) / 9801
    s = 0
    for i in range(k + 1):
        s_numerator = (math.factorial(4 * i) * (1103 + 26390 * i)) 
        s_denominator = (math.factorial(i)** 4 * (396 **(4 * i)))
        s += (s_numerator / s_denominator)
    return 1 / (a * s)


def main():
    terms = input("Enter the number of terms to use in the calculation of pi: ")
    print(pi(int(terms)))


if __name__ == "__main__":
    main()