# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        isEven = True
        q = deque([root])

        while q:
            prevVal = -math.inf if isEven else math.inf

            for _ in range(len(q)):
                node = q.popleft()

                if isEven:
                    if node.val % 2 == 0 or node.val <= prevVal:
                        return False

                else:
                    if node.val % 2 != 0 or node.val >= prevVal:
                        return False
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

                prevVal = node.val
            
            isEven = not isEven

        return True

        