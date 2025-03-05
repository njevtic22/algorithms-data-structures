from factorial import main as fact_main
from lines import main as draw_main


def main():
    menu_text = "1. Calculate factorial\n" \
                "2. Draw lines\n" \
                "0. Exit"
    menu = {
        1: fact_main,
        2: draw_main
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
