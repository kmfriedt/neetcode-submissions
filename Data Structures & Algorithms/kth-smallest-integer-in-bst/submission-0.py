# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None
        def dfs(node):
            # in order traversal
            if node.left:
                dfs(node.left)
        
            if self.count == k-1:
                self.result = node.val
            self.count += 1
            
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.result