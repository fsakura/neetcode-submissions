# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        mid = self.find_mid(head)
        t2 = self.reverse_list(mid)
        t = ListNode(0)
        t1 = head
        # t = head
        # t1 = head.next
        i = 0
        while t1 and t2:
            if i % 2 == 1:
                t.next = t2
                t2 = t2.next
            else:
                t.next = t1
                t1 = t1.next
            t = t.next
            i += 1
        t.next = t1 if t1 else t2

    def find_mid(self, node: ListNode) -> ListNode:
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return slow
    
    def reverse_list(self, node: ListNode) -> ListNode:
        temp = node
        prev = None
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        return prev
