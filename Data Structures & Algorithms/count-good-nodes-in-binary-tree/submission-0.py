# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0 
        max_val = -101 # lower than the node.val minimum described
        
        def dfs(node, max_value):
            if node.val >= max_value:
                self.good_nodes += 1
            max_value = max(max_value, node.val)
            if node.left:
                dfs(node.left, max_value)
            if node.right:    
                dfs(node.right, max_value)


        dfs(root, max_val)
        return self.good_nodes