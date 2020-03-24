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

    How to know the total number of nodes we have based on the level:
    Level 0: 2^0 = 1;
    Level 1: 2^1 = 2;
    Level 2: 2^2 = 4;
    Level 3: 2^3 = 8;

    # of nodes = 2^h - 1
    # log nodes = height/steps
    # log 100 = 100^2
    * h = height starts from count of 1
"""
"""
The left side is always the lower number.
https://visualgo.net/bn/bst
Balanced trees has operations O(log N), but unbalanced ones that keep adding
thing to the right side, became a O(N)
EX:
            101
               \
               105
               /  \
             102  144
                    \
                    231
                    
Balanced tree:
           101
          /    \
        33     105
       /  \   /    \
      9   37  104  144


BST = Binary Search Tree

Pros:
Better than O(n)
Ordered
Flexible Size

Cons:
No O(1) operations
"""
