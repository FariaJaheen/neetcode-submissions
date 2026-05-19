def add_two_numbers() -> int:
    line = input()
    line_int = line.split(",")
    add_2num = int(line_int[0]) + int(line_int[1])
    return add_2num


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
