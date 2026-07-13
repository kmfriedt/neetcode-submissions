# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.stack = []
        self.result = None
        self.k = k
        def dfs(node):
            self.stack.append(node.val)
            # in order traversal
            if node.left:
                dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = self.stack[-1]
            self.stack.pop()
            
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.result