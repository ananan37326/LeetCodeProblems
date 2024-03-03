# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, cur = head, head

        for _ in range(n):
            cur = cur.next

        if not cur:
            return head.next
        
        while cur.next:
            prev = prev.next
            cur = cur.next

        prev.next = prev.next.next

        return head

        