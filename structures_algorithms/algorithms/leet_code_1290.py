"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
Example 3:

Input: head = [1]
Output: 1
Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
Example 5:

Input: head = [0,0]
Output: 0
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @classmethod
    def getDecimalValue(self, head: ListNode) -> int:
        decimal_value = 0
        binary_numbers = []
        current_node = head
        while True:
            binary_numbers.append(current_node.val)
            if not current_node.next:
                break
            current_node = current_node.next

        for idx, binary in enumerate(reversed(binary_numbers)):
            decimal_value += binary*2**idx
        return decimal_value


linked_list = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]

new_node = ListNode(val=linked_list[0])
for node in linked_list[1:]:
    old_node = new_node
    new_node = ListNode(node)
    old_node.next = new_node

print(new_node.val)
print()
