def int_to_hex(n):
    def alphabet(char):
        if char in ['A','a']:
            return 10
        elif char in ['B','b']:
            return 11
        elif char in ['C','c']:
            return 12
        elif char in ['D' , 'd']:
            return 13
        elif char in ['E','e']:
            return 14
        elif char in ['F', 'f']:
            return 15
    try:
        return int(n)
    except Exception as e:
        return alphabet(n)



def hex_output():
    decnum = 0
    hexnum = input("Enter a hex number to convert: ")
    for power, digit in enumerate(reversed(hexnum)):
        print("Int to Hex", digit, int_to_hex(digit))
        print(f"{power+1} -> {int_to_hex(digit)} * {16**power}")
        decnum += int_to_hex(digit) * (16 ** power)

    assert decnum == int(hexnum, 16)
    print(decnum)

hex_output()