# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        if length == n:
            return head.next
        t2 = head
        for i in range(n):
            if not t2:
                return head
            t2 = t2.next
        t1 = head
        prev = None
        while t2:
            prev = t1
            t1 = t1.next
            t2 = t2.next

        prev.next = t1.next
        return head
        