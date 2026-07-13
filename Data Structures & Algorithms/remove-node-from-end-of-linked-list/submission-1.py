# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # find length of list

        slow, fast = head, head

        # move the fast pointer up
        for _ in range(n):
            fast = fast.next
  
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next


        if slow == head:
            head = head.next
        else:
            prev.next = slow.next

        return head