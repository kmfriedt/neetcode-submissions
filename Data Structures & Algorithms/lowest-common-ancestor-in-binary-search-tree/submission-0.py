# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # there is no link back to the ancestor
        # have to start at the root and look for the two nodes
        # need to have both nodes

        # check to see if the root node is one of p OR q

        # check the leaf nodes to see if they are p OR q

        # if we have both p AND q THEN we can return the current node

        # if not then we have to do a recursive search on the left and right node
        # all nodes are unique, there will always be an answer, there will always be
        # at least 2 nodes

        # Algorithm

            # need to pass up a tuple of bool (p, q) need both to be correct
            # recursive call to each leaf node and get the tuple back
            # need to set the value of p and q from both return types
            # need to update the value of p and q based on the local node
            # if both are true then we can return the node
            # need a separate dfs function
        self.ancestor = None
        def dfs(node: Optional[TreeNode]) -> tuple(bool, bool):
            if not node:
                return (False, False)

            left = dfs(node.left)
            right = dfs(node.right)

            # get a tuple from each
            # look at p
            is_p = (left[0] or right[0])
            # look at q
            is_q = (left[1] or right[1])

            if node.val == p.val:
                is_p = True
            if node.val == q.val:
                is_q = True

            if is_p and is_q and not self.ancestor:
                # need to set the node
                # how would we exit early or stop? 
                self.ancestor = node
            return (is_p, is_q)
        
        dfs(root)
        return self.ancestor