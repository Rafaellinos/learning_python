"""
reverse string by using
"""


def reverse_str(string):
    return string[::-1]

def reverse(string):
    print(string)
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

# print(reverse_str('hello'))
print(reverse('hello'))
