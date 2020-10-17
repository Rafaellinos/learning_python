"""Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
"""


def balance_string(string):
    pairs = 0
    ls = 0
    for el in string[::-1]:
        if el == 'L':
            ls += 1
        elif el == 'R':
            ls -= 1
        if ls == 0:
            pairs += 1
    return pairs


print(balance_string(string='RLLLLRRRLR'))
