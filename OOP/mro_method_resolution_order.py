"""
    mro is the order of which object inherited will be used.

    object
     |
     A
    / \
    B C
    \ /
     D

    order: D->B->C->A->object
    it uses the 'closest' one.
"""


class A(object):
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num) # output = 1, because C is more close
print(D.mro())
# output
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
"""
      object
    /  |    \
    X  Y    Z
    \ / \ /  /
     A   B  /
      \  | /
         M 
    order: M->B->A->X->Y->Z->object

    This happens bacause Z is more "far" and is on the same "line" as X,Y,Z
    even if M inherits Z, it will look at X and Y first.

"""

class X(object): pass
class Y(object): pass
class Z(object): pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass

print(M.mro()) 
# output 
# [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]