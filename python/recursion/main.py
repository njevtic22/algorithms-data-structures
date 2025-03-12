from array_sum import halved_main as halved_sum_main
from array_sum import linear_main as sum_main
from binary_search import main as binary_main
from factorial import main as fact_main
from fibonacci import cache_main as cache_fib_main
from fibonacci import exp_main as exp_fib_main
from fibonacci import lin_main as lin_fib_main
from lines import main as draw_main
from power import main_1 as power_1_main
from power import main_2 as power_2_main
from reverse_array import main as reverse_main


def main():
    menu_text = "Recursion examples\n" \
                "1. Calculate factorial\n" \
                "2. Draw lines\n" \
                "3. Binary search\n" \
                "4. Linear sum\n" \
                "5. Halved sum\n" \
                "6. Reverse array\n" \
                "7. Power 1 - multiplying each successive element\n" \
                "8. Power 2 - half^power\n" \
                "9. Fibonaci - exponential recursion\n" \
                "10. Fibonaci - exponential recursion with cache\n" \
                "11. Fibonaci - linear recursion\n" \
                "0. Exit"
    menu = {
        1: fact_main,
        2: draw_main,
        3: binary_main,
        4: sum_main,
        5: halved_sum_main,
        6: reverse_main,
        7: power_1_main,
        8: power_2_main,
        9: exp_fib_main,
        10: cache_fib_main,
        11: lin_fib_main
    }

    while True:
        print(menu_text)
        option = int(input("Enter number of desired option: "))
        if option == 0:
            return

        print()
        menu[option]()
        print()


if __name__ == '__main__':
    main()
