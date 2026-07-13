# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None
        root = TreeNode(val=preorder[0])
        index = 0
        while inorder[index] != root.val:
            index += 1
        # now we have the index
        if len(preorder) > 0 and len(inorder) > 0:
            left = self.buildTree(preorder[1:index+1], inorder[0:index])
            right = self.buildTree(preorder[index+1:], inorder[index+1:])
            root.left = left
            root.right = right

        return root