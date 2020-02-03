
try: 
    with open("test1.txt", mode="r+") as f:
        text = f.write('hey, its me!')
except FileNotFoundError as err:
    print('File does not exist')
except IOError as err:
    raise err