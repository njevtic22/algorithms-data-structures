def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)


def main():
    n = int(input("Enter number: "))
    if n < 0:
        raise AttributeError("Fibonaci argument must be positive integer")

    value = fact(n)
    print("fact(", n, ")", " = ", value, sep="")
