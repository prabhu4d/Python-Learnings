class Char:
    """
    A set of symbols to represents ascii characters

    A ->     ++
            +  +
           ++++++
          +      +
         +        +

    char box = (9, 5)
    """

    A = [
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    B = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    ]

    C = [
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    chars = {"A": A, "B": B, "C": C}

    def __init__(self, char, symbol):
        self.char = char
        self.symbol = symbol

    def __str__(self):
        asc_ii = ""
        for row in self.chars[self.char]:
            for digit in row:
                if digit:
                    asc_ii += self.symbol
                else:
                    asc_ii += " "
            asc_ii += "\n"
        return asc_ii
