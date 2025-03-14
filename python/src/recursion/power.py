from time import time


def power_1(x, n):
    """
    x^n = x*x*x* ... *x -> array
    This function calculates power by multiplying each successive element recursively.

    :param x: base
    :param n: exponent
    :return: result of power operation
    """
    if n == 1 or x == 0:
        return x

    return x * power_1(x, n - 1)


def power_2(x, n):
    """
    x^n = x*x*x* ... *x -> array
    This function calculates power by calculating power of half of the array recursively
    and then raising it to power of 2.

    :param x: base
    :param n: exponent
    :return: result of power operation
    """
    if n == 1 or x == 0:
        return x

    if n % 2 == 0:
        result = power_2(x, n // 2)
        return result ** 2
    else:
        result = power_2(x, (n - 1) // 2)
        return result ** 2 * x


def get_input():
    x = int(input("Enter base: "))
    n = int(input("Enter exponent: "))

    if n < 0:
        x = 1/x
        n = -n

    return x, n


def main_1():
    x, n = get_input()

    start = time()
    result = power_1(x, n)
    end = time()
    print(x, "^", n, "=", result)
    print("Execution time:", end - start)


def main_2():
    x, n = get_input()

    start = time()
    result = power_2(x, n)
    end = time()
    print(x, "^", n, "=", result)
    print("Execution time:", end - start)
