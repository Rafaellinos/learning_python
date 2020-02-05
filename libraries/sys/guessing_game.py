import sys
import random
"""
Run the file and give 2 params. The game will generate a number between these two number
and you have to type the write one to exit the game.
ex:
python3 guessing_game.py <num1> <num2>
"""

def _get_nums():
    """Get numbers from param ex: python3 file.py 1 100"""
    try:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])
        return n1, n2
    except ValueError as err:
        return "The param must be an integer number"
    except Exception as err:
        return f"No param givem! {err}"


def _randomize(n1=0, n2=1):
    """return a number betwen n1 and n2"""
    if not isinstance(n1, int) and not isinstance(n2, int):
        return "Must be int"
    elif (n1 is None) or (n2 is None):
        return "Cannot have None object"
    elif (type(n1) == bool) or (type(n2) == bool):
        return "Must be int"
    try:
        return random.randint(n1, n2)
    except ValueError as err:
        return err


def main():
    try:
        n1, n2 = _get_nums()
    except Exception as err:
        return f"Erro {err}"

    random_number = _randomize(n1, n2)

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
    
if __name__ == '__main__':
    main()