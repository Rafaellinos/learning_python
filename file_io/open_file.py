"""
how to open file with python
"""

with open("test.txt") as f: # defult is mode r
    print(f)
    # output:
    # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
    print(f.read())
    f.seek(0) # move cursor back, without this, the next read will return blank
    print(f.read()) 
    # can only read the file ONCE, because the cursor
    f.seek(0)
    print(f.readline())
    print(f.readline())
    print(f.readline())
    f.seek(0)
    print(f.readlines()) # return a list of lines
