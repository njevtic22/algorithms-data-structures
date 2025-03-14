from time import time

from src.util.arrays import generate_array


def linear_sum(data, n):
    if n == 1:
        return data[0]

    return data[n - 1] + linear_sum(data, n - 1)


def halved_sum(data, low, high):
    """
    Calculates sum of array by calculating sums of its two halves.
    Works in O(log(n)) time ?

    :param data: input array
    :param low: lower bound
    :param high: upper bound
    :return: sum of elements from lower bound up to upper bound
    """
    if low == high:
        return data[low]

    low1 = low
    high1 = (low + high) // 2

    low2 = high1 + 1
    high2 = high

    return halved_sum(data, low1, high1) + halved_sum(data, low2, high2)


def linear_main():
    data = generate_array(50)
    start = time()
    summed = linear_sum(data, len(data))
    end = time()

    print("Sum of array is", summed)
    print("Execution time:", end - start)


def halved_main():
    data = generate_array(50)
    start = time()
    summed = halved_sum(data, 0, len(data) - 1)
    end = time()

    print("Sum of array is", summed)
    print("Execution time:", end - start)
