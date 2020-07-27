"""Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
"""

def balance_string(string):
    pairs = 0
    balance_check = ''
    for i, ele in enumerate(string):
        if balance_check == 'R' and string[i] == 'L':
            pairs += 1
            balance_check = ''
        elif balance_check == 'L' and string[i] == 'R':
            pairs += 1
            balance_check = ''
        elif balance_check == 'R' and string[i] == 'R':
            balance_check = ''
        
        
    pass


s = 'RLRRLLRLRL'
