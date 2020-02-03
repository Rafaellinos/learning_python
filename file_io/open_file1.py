

"""
modes:
r = only read
w = only write, and overwrite everything because it dont read what is there, also creates a file
r+ = read and write and dont erase what is there
a = append mode, adds to the end of the file
"""
with open("test.txt", mode="r+") as f:
    text = f.write('hey, its me!')
    print(text) # output 12, because 12 characters
    text = f.write(':)')
    print(text) 
    # output 2, because 2 characters.
    # hey, its me!:), the cursor is not at the end
    # if open the file again, the text will be the first
    # because when u open the file, the cursos default location
    # is on the first position.

with open("test.txt", mode="a") as file:
    text = file.write("end")
    print(text) # hey, its me!:)end