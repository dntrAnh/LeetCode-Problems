# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return False 
        
        queue = deque([(root, root.val)])
        
        while queue:
            node, curr_sum = queue.popleft()
            
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    return True
            
            if node.left:
                queue.append((node.left, curr_sum + node.left.val))
            if node.right:
                queue.append((node.right, curr_sum + node.right.val))
        
        return False
