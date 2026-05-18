def first_n_characters(s: str, n: int) -> str:
    for i in range(len(s)):
        if len(s)>= n: 
            return s[i:]

def last_n_characters(s: str, n: int) -> str:
    if len(s)>= n:
        return s[len(s)-n]


# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))
