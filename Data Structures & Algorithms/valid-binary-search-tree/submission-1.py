# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True

        def dfs(node) -> tuple(int, int): # (min_val, max_val)
            min_val, max_val = node.val, node.val
            if node.left:
                left = dfs(node.left)
                # need the max value from the left
                if node.val <= left[1]: # the max value
                    self.is_valid = False
                min_val = min(node.val, left[0])
            if node.right:
                right = dfs(node.right)
                # need the min value from the right
                if node.val >= right[0]:
                    self.is_valid = False
                max_val = max(node.val, right[1])
            return (min_val, max_val)

        dfs(root) 
        
        return self.is_valid
            