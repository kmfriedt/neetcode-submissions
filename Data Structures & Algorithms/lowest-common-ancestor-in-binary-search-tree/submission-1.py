# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # a binary search tree has certain qualities we can exploit

        # we have the values, we need a node where the values exist below it

        # we need to find the smaller and larger value of p and q
        small_value = min(p.val, q.val)
        large_value = max(p.val, q.val)
        
        node = root

        while node:
        
            # we need to find a node where the left node is greater than or equal to small value
            # and where the right node is less than or equal to the large value
            if small_value <= node.val and large_value >= node.val:
                return node
        
            # if the large_value is less than the current node then we need to look at
            # the left sub tree
            if large_value < node.val:
                node = node.left

            # if the small_value is greater than the current node then we need to look at
            # the right sub tree
            if small_value > node.val:
                node = node.right


        


