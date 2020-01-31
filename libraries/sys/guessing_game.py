import sys
import random
"""
Run the file and give 2 params. The game will generate a number between these two number
and you have to type the write one to exit the game.
ex:
python3 guessing_game.py <num1> <num2>
"""
try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
except ValueError as err:
    print(f"The param must be an integer number")
    exit()
except Exception as err:
    print(f"No param givem! {err}")
    exit()



random_number = random.randint(int(n1), int(n2))
print(random_number)
while 1:
    try:
        number = int(input(f"Type a number between {n1} and {n2}:\n"))
        if not n1 <= number <= n2:
            print(f"The number must be between {n1} and {n2}!")
        elif number == random_number:
            print("Congratulations!")
            break
        else:
            print("Wrong! Keep trying")
    except:
        print(f"Must be an integer number!")
    


