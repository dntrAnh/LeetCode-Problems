# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        if root is None:
            return result
        
        to_delete_set = set(to_delete)
        
        def delete(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None
            
            node.left = delete(node.left)
            node.right = delete(node.right)
            
            if node.val in to_delete_set:
                if node.left:
                    result.append(node.left)
                if node.right:
                    result.append(node.right)
                return None
            
            return node
        
        root = delete(root)
        if root:
            result.append(root)
        
        return result
