#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if len(p) == 1 or p[1] != '*':
            if len(s) < 1 or (s[0] != p[0] and p[0] != '.'):
                return False
            return self.isMatch(s[1:], p[1:])
        while len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
        return self.isMatch(s, p[2:])
        
        
# @lc code=end

