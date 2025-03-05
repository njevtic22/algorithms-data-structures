def draw(length):
    if length <= 0:
        return

    draw(length // 2)
    print("-" * length)
    draw(length // 2)


def draw_lines(length):
    print("-" * length)
    draw(length // 2)
    print("-" * length)


def main():
    length = int(input("Enter max line length: "))
    if length <= 0:
        raise AttributeError("Max line length must be positive integer")

    draw_lines(length)
