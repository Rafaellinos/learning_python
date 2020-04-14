"""
Graph DAG
Directed Acyclic graph
"""
"""
    2 - 0
   / \
  1 - 3  
"""
# Edge list:
graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacent list:
graph = {
    0: [2], # 0 is connected with 2
    1: [2,3], # 1 is connected with 2 and 3 and so on
    2: [0,1,3],
    3: [1,2]
}

# Adjacent Matrix:
graph = [
    [0, 0, 1, 0], # item 0 is connected with node 2 (index 2)
    [0, 0, 1, 1], # item 1 is connected with node 2 and 3 (index 2, 3)
    [1, 1, 0, 1], # item 2 is connected with node 0, 1 and 3 (index 0,1,3)
    [0, 1, 1, 0]  # item 3 is connected with node 1 and 2 (index 1,2)
]