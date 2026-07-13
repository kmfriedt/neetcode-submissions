# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # find length of list

        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next

        index = length - n

        cur = head
        for _ in range(index):
            prev = cur
            cur = cur.next

        if cur == head:
            head = head.next
        else:
            prev.next = cur.next

        return head