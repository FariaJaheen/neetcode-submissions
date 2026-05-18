def remove_fourth_character(word: str) -> str:
    fourth_character = word[:3]
    after_fourth = word[4:]
    new_msg =  word[:3] + word[4:]
    return new_msg
# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
