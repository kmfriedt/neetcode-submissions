# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # base case
        if not root:
            return root

        # sub tree we want the right node to equal the left node vice versa
        temp = root.left
        root.left = root.right
        root.right = temp

        # now we need to process each subtree
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root