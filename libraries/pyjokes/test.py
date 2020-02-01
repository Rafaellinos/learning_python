import pyjokes


try:
    n = int(input("How many jokes?"))
    for i in range(n):
        print(pyjokes.get_joke('en', 'neutral'))
except ValueError:
    print("Must be an integer number!")
