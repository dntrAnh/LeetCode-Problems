"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: 
            return []
        
        result = []

        def dfs(node): 
            for nodes in node.children: 
                dfs(nodes) 
            result.append(node.val)
        
        dfs(root)
        return result
