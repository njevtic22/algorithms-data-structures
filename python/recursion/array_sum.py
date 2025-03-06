from time import time

from util import generate_array


def linear_sum(data, n):
    if n == 1:
        return data[0]

    return data[n - 1] + linear_sum(data, n - 1)


def main():
    data = generate_array(50)
    start = time()
    summed = linear_sum(data, len(data))
    end = time()

    print("Sum of array is", summed)
    print("Execution time:", end - start)
