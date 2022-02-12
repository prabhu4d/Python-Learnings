def print_char(name):
    print(name)
    if len(name) == 0:
        return
    return print_char(name[1:])


print_char("PRABHU")
