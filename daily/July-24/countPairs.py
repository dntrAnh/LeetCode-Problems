# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0

        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [1]

            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            for l in left_dist:
                for r in right_dist:
                    if l + r <= distance:
                        self.result += 1

            return [d + 1 for d in left_dist + right_dist]

        dfs(root)
        return self.result
