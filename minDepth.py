# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 
        
        queue = deque([root])
        level = 0
        
        while queue: 
            level += 1
            for _ in range(len(queue)): 
                node = queue.popleft() 
                if not node.left and not node.right: 
                    return level
                for child in [node.left, node.right]: 
                    if child:
                        queue.append(child) 

        return level 
