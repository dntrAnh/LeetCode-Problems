# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    stack = []

    def __init__(self, root: Optional[TreeNode]):
        self.build_tree(root)

    def next(self) -> int:
        temp = self.stack.pop() 
        self.build_tree(temp.right) 
        return temp.val 

    def hasNext(self) -> bool:
        return True if self.stack else False 
        
    def build_tree(self, root): 
        while root: 
            self.stack.append(root)
            root = root.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
