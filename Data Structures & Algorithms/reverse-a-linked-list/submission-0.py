# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        node_values = []

        ptr = head

        while ptr:
            node_values.append(ptr.val)
            ptr = ptr.next

        # now have a list of values
        print(node_values)
        new_list = ListNode()
        ptr = new_list
        for i in range(len(node_values)-1, 0, -1):
            print(node_values[i])
            ptr.val = node_values[i]
            ptr.next = ListNode()
            ptr = ptr.next

        ptr.val = node_values[0]
        ptr.next = None

        return new_list
        