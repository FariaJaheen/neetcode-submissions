def first_n_characters(s: str, n: int) -> str:
    if len(s)>= n:
        return s[0]

def last_n_characters(s: str, n: int) -> str:
    if len(s)>= n:
        return s[n-1]


# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))
