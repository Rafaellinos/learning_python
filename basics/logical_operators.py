# ==, <= , >=, <, >, and, or, !=, <>.

is_magician = True
is_expert = False

if not is_magician: # if False
    print("You need magic powers!")
elif is_expert and is_magician: # if True and True
    print("You are magician and expert!")
elif is_magician and not is_expert: # if True and False
    print("You are magician, but not expert")
"""
    elif is_magician and not(is_expert)
    same thing
"""

print(not(True)) 
# not reverts the result

## '==' evaluate to bool, example: print(True == 1) is the same thing as print(True == bool(1))
## 'is' checks if the location in the memory is the same.