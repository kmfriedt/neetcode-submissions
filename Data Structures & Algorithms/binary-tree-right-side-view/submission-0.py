# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # right side view is essentially the most right node at any level

        # so we have to go through and each level and add the right node first
        # then the left node

        # then per each level we only add the first node to the result

        # there can be no nodes in the tree

        if not root:
            return []

        from collections import deque # for level order traversal

        deq = deque()
        deq.append(root)
        result = []
        while deq:
            for i in range(len(deq)):
                node = deq.popleft()
                if i == 0:
                    result.append(node.val)
                if node.right:
                    deq.append(node.right)
                if node.left:
                    deq.append(node.left)
        
        return result