from time import time


def exp_fib(n):
    """
    Calculates fibonacci number by recursively calculating and then summing two previous fibonacci numbers.
    Works in O(2^n) time because it has two recursive calls for each fibonacci number.

    :param n: fibonacci number to be calculated
    :return: value of fibonacci number
    """
    if n <= 2:
        return 1

    return exp_fib(n - 1) + exp_fib(n - 2)


def exp_fib_cache(n, cache: dict):
    """
    Calculates fibonacci number by recursively calculating and then summing two previous fibonacci numbers.
    This version uses dictionary as cache, that way previously calculated fibonacci numbers are cached so that
    they are not calculated again.
    Size of cache is limited to certain amount of most recently calculated fibonacci numbers.

    :param n: fibonacci number to be calculated
    :param cache: cache of most recent calculated fibonacci numbers
    :return: value of fibonacci number
    """
    if n <= 2:
        return 1

    if n in cache:
        return cache[n]

    value = exp_fib_cache(n - 1, cache) + exp_fib_cache(n - 2, cache)

    cache[n] = value
    if len(cache) > 2:
        remove = min(cache, key=cache.__getitem__)
        del cache[remove]

    return value


def lin_fib(n):
    """
    Calculates fibonacci number by recursively calculating previous fibonacci number.
    Works in O(n) time because it has single recursive call for each fibonacci number.

    :param n: fibonacci number to be calculated
    :return: pair of desired fibonacci number and its predecessor
    """
    if n <= 2:
        return 1, 1

    i, j = lin_fib(n - 1)
    return i + j, i


def execute_fib(fib, n):
    start = time()
    value = fib(n)
    end = time()

    print(n, "fibonacci number is:", value)
    print("Execution time:", end - start, "seconds")
    print()


def exp_main():
    n = int(input("Enter desired fibonacci number: "))
    execute_fib(exp_fib, n)


def cache_main():
    n = int(input("Enter desired fibonacci number: "))
    execute_fib(lambda x: exp_fib_cache(x, {}), n)


def lin_main():
    n = int(input("Enter desired fibonacci number: "))
    execute_fib(lin_fib, n)

