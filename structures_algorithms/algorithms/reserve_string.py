"""
Reverse the string

"""

def reverse_string(string_to_reverse: str) -> str:
    if not isinstance(string_to_reverse, str) or string_to_reverse.__len__() < 2:
        return string_to_reverse
    new_string = str()
    index = string_to_reverse.__len__()-1
    j = 0
    while(j <= index):
        new_string += string_to_reverse[index]
        index -= 1
    return new_string


print(reverse_string("hi my name is rafael"))