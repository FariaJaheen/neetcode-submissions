from typing import List

def read_integers() -> List[int]:
    line = input()
    line_list = line.split(",")
    list_int = []
    for string in line_list:
        list_int.append(int(string))
    return list_int
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
