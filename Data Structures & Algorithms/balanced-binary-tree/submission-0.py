# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # need two things here

        # need to return a result for each node of whether it is balanced
        self.balanced = True # set this to True

        # need to return a height for each sub tree
        # need a dfs function
        def dfs(node: Optional[TreeNode]) -> int:
            # needs to return the max height of the two sides
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            # need to evaluate if this node is balanced
            if abs(left - right) > 1:
                self.balanced = False
            return 1 + max(left, right)

        dfs(root)
        
        return self.balanced