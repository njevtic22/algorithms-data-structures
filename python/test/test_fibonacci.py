from src.recursion.fibonacci import exp_fib, exp_fib_cache, lin_fib
from src.util.cell_printer import CellPrinter
from time import time


def main():
    fibs = [exp_fib, lambda n: exp_fib_cache(n, {}), lin_fib]
    # fibs = [lambda n: "/", lambda n: exp_fib_cache(n, {}), lin_fib]

    cell = CellPrinter(["Fibonaci number", "exp_fib", "exp_fib_cache", "lin_fib"], [17, 30, 30, 30])
    cell.print_header()

    for n in range(0, 55, 5):
        cell.print(str(n))

        for fib in fibs:
            start = time()
            fib(n)
            end = time()
            cell.print(str(end - start))


if __name__ == '__main__':
    main()
