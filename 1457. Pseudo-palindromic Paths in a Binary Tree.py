# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = defaultdict(int)
        odd = 0

        def inorder(current):
            nonlocal odd

            if not current:
                return 0
            
            count[current.val] += 1
            odd_change = 1 if count[current.val] % 2 == 1 else -1

            odd += odd_change

            if not current.left and not current.right:
                res = 1 if odd <=1 else 0
            else:
                res = inorder(current.left) + inorder(current.right)

            count[current.val] -= 1
            odd -= odd_change
            return res

        return inorder(root)
        