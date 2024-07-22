# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(root, target): 
            queue = deque([root])
            path = []
            visited = set()
            node = root

            while queue: 
                if node and node.val == target: 
                    return path 
                if node.left and node.left not in visited: 
                    queue.append(node) 
                    path.append('L') 
                    node = node.left 
                elif node.right and node.right not in visited: 
                    queue.append(node) 
                    path.append('R') 
                    node = node.right
                else: 
                    visited.add(node) 
                    path.pop() 
                    node = queue.pop() 
        start_path = dfs(root, startValue) 
        dest_path = dfs(root, destValue) 

        i = 0
        while i < min(len(start_path), len(dest_path)): 
            if start_path[i] != dest_path[i]: 
                break 
            i += 1
        
        result = 'U' * (len(start_path) - i) + ''.join(dest_path[i:])
        return result
