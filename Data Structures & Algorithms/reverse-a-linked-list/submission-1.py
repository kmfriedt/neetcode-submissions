# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        # need three pointers to do this so we don't lose nodes

        prev = None # new end
        cur = head # current node
        temp = cur.next

        while cur:
            cur.next = prev
            prev = cur
            cur = temp
            if cur:
                temp = cur.next
        
        return prev
        