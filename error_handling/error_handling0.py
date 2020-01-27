##
# 
# 
# 
while True:
    try:
        age = int(input('what is your age: '))
        10/age
        print(age)
    except ZeroDivisionError:
        print("Age can't be zero")
        continue # it continues on the loop with out without continue
    except ValueError:
        print("Please enter a number")
        break # exit the loop if value error
    else: #enter on this else when try is sucefully
        print("thank you")
        break # to exit loop if try gets no error
    finally: # finally runs no matter what
        print("fainally done")

    print("you got me") # can't get here because of the breaks and continues