class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0

        while left != right:
            left = left >> 1
            right = right >> 1
            count += 1

        return right << count
        