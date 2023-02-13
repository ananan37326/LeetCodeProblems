#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {}

        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            
            copy_node = Node(node.val)

            hashmap[node] = copy_node

            for nei in node.neighbors:
                copy_node.neighbors.append(dfs(nei))

            return copy_node


        return dfs(node) if node else None 
        
# @lc code=end

