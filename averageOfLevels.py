# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: 
            return []
            
        def average_calculate(arr): 
            curr_sum = sum(arr)
            return curr_sum / len(arr)
        
        queue = deque([root])
        result = []
        
        while queue: 
            level = []
            for _ in range(len(queue)): 
                node = queue.popleft() 
                level.append(node.val)
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            result.append(average_calculate(level))
        
        return result 
