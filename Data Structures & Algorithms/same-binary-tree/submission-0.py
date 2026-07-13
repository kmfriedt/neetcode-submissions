# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same_tree = True

        def dfs(node1, node2):
            if not node1 and not node2:
                return
            if node1 and node2:
                if node1.val != node2.val:
                    self.same_tree = False
                else:
                    dfs(node1.left, node2.left)
                    dfs(node1.right, node2.right)

            else:
                # one of the two nodes is None
                self.same_tree = False

        dfs(p, q)
        return self.same_tree