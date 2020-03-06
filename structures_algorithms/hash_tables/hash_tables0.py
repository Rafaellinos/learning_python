"""
    Hash function is one way, it means that u can't discovery what is the input
    by just seen the output. And no matter how many characters your input has,
    the output will always have the same value. Idempotent
    Example:
        md5:
            input string -> hello
            output hash  -> 5d41402abc4b2a76b9719d911017c592
"""

user = {
    'age': 54,
    'name': 'Kylie',
    'magic': True,
    'scream': lambda: print("ahhhh")
}

print(user['age']) # O(1)
print(user['scream']()) # O(1)

"""
problem with hash: Hash Collisions
https://www.cs.usfca.edu/~galles/visualization/OpenHash.html

Hash table (hash map) is a data structure that implements an associative array 
abstract data type, a structure that can map keys to values. A hash table uses 
a hash function to compute an index, also called a hash code, into an array of 
buckets or slots, from which the desired value can be found.

Ideally, the hash function will assign each key to a unique bucket, but most 
hash table designs employ an imperfect hash function, which might cause hash 
collisions where the hash function generates the same index for more than one 
key. Such collisions are always accommodated in some way.


Collision resolution: Separate chaining
When the hash function put something in a busy place, it creates
a linked list, and every time that we try to access that item,
we need to loop through the linked list to find what we need.
And that's what slows down the access memory. 

With collision and liked lists, we have O(n) operation.
"""
