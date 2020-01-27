##

while True:
    try:
        age = int(input('what is your age: '))
        raise Exception('wrong') 
        # can raise any kind of exception
        # is usefull when u need to build your own exception
    except ValueError as err:
        raise ValueError('sdasjkdhasdh')
    else:
        print("thank you")
        break
