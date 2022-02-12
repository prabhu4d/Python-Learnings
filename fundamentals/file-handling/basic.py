"""
File Handling

"""

# Normal way of open a file
# you have to manually close the file
# f = open("python.txt", 'r')
# print(f.name)
# print(f.mode)
# f.close()

print("\nContext Manager")
# with context manager
with open('python.txt', 'r') as file:
    # it reads the entire file
    # file_content = file.read()

    # it reads entirely and makes list
    # file_content = file.readlines()

    # read line by line
    # file_content = file.readline()
    # print(file_content, end='')

    # loading line by line (it is iterator)
    # for line in file:
    # print(line, end='')

    # read by specific characters
    size_to_read = 30
    file_content = file.read(size_to_read)
    while len(file_content) > 0:
        # tells shows reading character position
        print(file_content, end=f'{{-{file.tell()}-}}')
        file_content = file.read(size_to_read)

    print("\n")
    # Again start the initial position to read characters
    file.seek(0)
    print(file.read())

# print(file.closed)


# copying file
with open('python.txt', 'r') as rf:
    with open('python_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# to work with images, audios use 'rb', 'wb'