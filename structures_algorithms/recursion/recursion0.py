counter = 0
def inception():

    # block to avoid cause overflow
    global counter
    if counter > 3:
        return 'done!'
    counter += 1
    print(counter)
    ####

    return inception()

inception()
# can cause stack overflow when reach the limit of call stacks in memory.

"""
Traceback (most recent call last):
  File "recursion0.py", line 4, in <module>
    inception()
  File "recursion0.py", line 2, in inception
    inception()
  File "recursion0.py", line 2, in inception
    inception()
  File "recursion0.py", line 2, in inception
    inception()
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
"""