
class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return self

        obj = self.root
        while True:
            if value < obj.value:
                if not obj.left:
                    obj.left = new_node
                    break
                obj = obj.left
            else:
                if not obj.right:
                    obj.right = new_node
                    break
                obj = obj.right
        return self

    def lookup(self, value):
        # obj = self.root
        # while True:
        #     if obj == None:
        #         return False
        #     elif obj.value == value:
        #         return obj.value
        #     else:
        #         if value < obj.value:
        #             obj = obj.left
        #         else:
        #             obj = obj.right
        obj = self._traverse(value)
        if obj:
            return obj.value
        return False

    def _traverse(self, value):
        obj = self.root
        while obj:
            if value < obj.value:
                obj = obj.left
            elif value > obj.value:
                obj = obj.right
            elif value == obj.value:
                return obj
        return

    def remove(self, value):
        if not self.root:
            return False

        current = self.root
        parent = None
        while True:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            elif value == current.value:
                # option 1
                if not current.right:
                    if not parent:
                        self.root = current.left
                        break
                    if current.value < parent.value:
                        parent.left = current.left
                        break
                    elif current.value > parent.value:
                        parent.right = current.left
                        break
                elif not current.right.left:
                    current.right.left = current.left
                    if not parent:
                        self.root = current.right
                    else:
                        if current.value < parent.value:
                            parent.left = current.right
                        elif current.value > parent.value:
                            parent.right = current.right
                else:
                    leftmost = current.right.left
                    leftmost_parent = current.right
                    while not leftmost_parent:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left
                    
                    leftmost_parent.left = leftmost.right
                    leftmost.left = current.left
                    leftmost.right = current.right

                    if not parent:
                        self.root = leftmost
                    else:
                        if current.value < parent.value:
                            parent.left = leftmost
                        elif current.value > parent.value:
                            parent.right = leftmost
            return True

        
"""
       9
    4     20
  1   6  15  170
  
  insert 9
  insert 4
  insert 6
  insert 20
  insert 170
  insert 15
  insert 1
"""
bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
print(bst.lookup(88))
