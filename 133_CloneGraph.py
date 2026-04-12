"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        visited = {}

        def dfs(cur):
            if cur in visited:
                return visited[cur]
            
            clone = Node(cur.val)
            visited[cur] = clone

            for neigh in cur.neighbors:
                clone.neighbors.append(dfs(neigh))
            
            return clone
        
        return dfs(node)