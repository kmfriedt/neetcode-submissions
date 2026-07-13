"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = dict()
        from collections import deque
        deq = deque()
        root_node = Node(node.val, node.neighbors.copy())
        deq.append(root_node)
        visited[node.val] = root_node
        while deq:
            for _ in range(len(deq)):
                node = deq.popleft()
                new_neighbors = list()
                for neighbor in node.neighbors:
                    if neighbor.val not in visited:
                        new_node = Node(neighbor.val, neighbor.neighbors.copy())
                        new_neighbors.append(new_node)
                        deq.append(new_node)
                        visited[new_node.val] = new_node
                    else:
                        new_neighbors.append(visited[neighbor.val])
                node.neighbors = new_neighbors

        

        return root_node