# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        nodes = deque([root])
        bottomLeft = root.val

        while nodes:
            cur = nodes.popleft()
            bottomLeft = cur.val

            if cur.right:
                nodes.append(cur.right)
            if cur.left:
                nodes.append(cur.left)

        return bottomLeft
        