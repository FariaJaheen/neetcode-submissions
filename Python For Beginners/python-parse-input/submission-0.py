from typing import List

def read_integers() -> List[int]:
    num_string = "1,2,3,4,5"
    num_list = num_string.split(",")
    return num_list
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
