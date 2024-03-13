# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = dummy
        
        preSumToNode = {}
        preSum = 0

        while current:
            preSum += current.val

            if preSum in preSumToNode:
                prev = preSumToNode[preSum]

                current = prev.next

                p = preSum + current.val
                while p != preSum:
                    del preSumToNode[p]
                    current = current.next
                    p += current.val
                
                prev.next = current.next
            else:
                preSumToNode[preSum] = current
            
            current = current.next
        
        return dummy.next
        