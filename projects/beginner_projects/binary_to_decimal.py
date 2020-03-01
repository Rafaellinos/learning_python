"""
User Stories:
User can enter up to 8 binary digits in one input field
User must be notified if anything other than a 0 or 1 was entered
User views the results in a single output field containing the decimal (base 10)
 equivalent of the binary number that was entered
"""
import re

binary_number = input("Type a binary number: ")

pattern = re.compile(r"[a-zA-Z2-9\W]")

found = pattern.search(binary_number)

if found:
    print("To transform binary number into a decimal number you can only type 0s and 1s.")
    exit()


def convert_number(binary_number: str) -> str:
    total = int()
    exponent = int()
    for x in binary_number[::-1]:
        total += (2**exponent)*int(x)
        exponent += 1
    return str(total)

result = convert_number(binary_number)
print(f"The decimal number of {binary_number} is {result}")
print(result)
exit()

