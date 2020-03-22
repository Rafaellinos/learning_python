"""
Trees:

    example:

                  while
              /          \
            less         assign
           /  \         /       \
    variable iconst   variable  plus
        ....

    Perfect Binary Tree = All parents have two children's.
    Full binary tree = Incomplete binary tree, some parents have only one
    child.

    Operations:

        lookup : O(log N)
        insert : O(log N)
        delete : O(log N)

    Levels to calculate:
    Level 0: 2^0 = 1;
    Level 1: 2^1 = 2;
    Level 2: 2^2 = 4;
    Level 3: 2^3 = 8;

    # of nodes = 2^h - 1
    # log nodes - height(steps)
    * h = height starts from count of 1
"""

