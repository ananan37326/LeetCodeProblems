class Solution:
    def minimumMoves(self, s: str) -> int:
        res = i = 0

        while i < len(s):
            if s[i] == 'X':
                res += 1
                i += 3
            else:
                i += 1

        return res
        