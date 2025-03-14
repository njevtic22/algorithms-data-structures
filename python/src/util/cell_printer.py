def center(cell, width):
    return cell.center(width)


class CellPrinter:
    def __init__(self, header, widths):
        self.cell_counter = 0
        self.header = header
        self.widths = widths

        self.line = "".join(["+" + "-" * width for width in self.widths])
        self.line += "+"

        # builder = ["+"]
        # for width in self.widths:
        #     builder.append("-" * width)
        #     builder.append("+")
        # self.line = ''.join(builder)

    def has_header(self):
        return len(self.header) > 0

    def print_header(self):
        print(self.line)
        for i in range(len(self.header)):
            print("|", self.header[i].center(self.widths[i]), sep="", end="")
        print("|")
        print(self.line)

    def print(self, cell):
        width = self.widths[self.cell_counter]
        self.cell_counter = (self.cell_counter + 1) % len(self.widths)

        print("|", cell.center(width), sep="", end="")

        if self.cell_counter == 0:
            print("|")
            print(self.line)

    def clear(self):
        self.cell_counter = 0
        self.header.clear()
        self.widths.clear()
        self.line = ""
