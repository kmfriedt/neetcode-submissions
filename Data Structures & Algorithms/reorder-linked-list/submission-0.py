# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast, slow = head, head

        # find the middle 
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next

        # now the start of the right section will be slow.next
        # referse the right section
        prev = None
        cur = slow.next
        # have to unlink the first half from the second half
        slow.next = None

        while cur:
            temp = cur.next # this will be None at the end
            cur.next = prev
            prev = cur
            cur = temp

        ptr = prev
        while ptr:
            print(f"ptr: {ptr.val}")
            ptr = ptr.next


        # now prev points to the start of the reversed right side
        # now alternate the nodes

        ptr = head
        while ptr and prev: 
            temp1 = ptr.next
            temp2 = prev.next
            ptr.next = prev
            prev.next = temp1
            ptr = temp1
            prev = temp2


        