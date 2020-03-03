"""
Operations:
    Insertion: Insert a new item in the data structure.
    Deletion: Delete a data.
    Traversal: Access each data item one time.
    Search: Search for the data.
    Sorting: Organize data.
    Access: How to access the data.

Types:
    Arrays or Lists: Organize the data in order(index)
        Operations:
            lookup: O(1) -> python -> x in s O(n)
            push: O(1) -> python -> append O(1)
            insert: O(n) -> python -> insert O(n)
            delete: O(n) -> python -> O(n)
"""

# each variable has 4 spaces of 8 bits in a 32 operational system
# in a 64 system, each item has 8 spaces of bytes. 8 bits = byte
# so, each variable has:
# 8x4 = 32 bits in a 32-bits system
# 8x8 = 64 bits in a 32-bits system
strings = ['a', 'b', 'c', 'd']
# in this case, we have 4x8 = 64 bytes of usage
# 4 is each item in the list
# 8 is for each byte
strings[2]  # grab the 3 item where is stored in memory #O(1)

"""
 Difference between static and dynamic arrays:
    static arrays have the size specified, while dynamic can
    be allocate without specify the size and adding items.
    
    static -> int a[20]
    int b[5] {1,2,3,4,5}
"""


