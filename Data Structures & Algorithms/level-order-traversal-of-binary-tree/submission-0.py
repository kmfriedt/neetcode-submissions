# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        # need to use a dequeue 
        result = []
        if not root:
            return result
        deq = deque()
        deq.append(root)
        
        while deq:
            cur_level = list()
            for _ in range(len(deq)):
                node = deq.popleft()
                cur_level.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            result.append(cur_level)

        return result