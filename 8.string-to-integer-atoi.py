#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        sum = 0
        isNeg = False
        max_val = 2**31
        min_val = -1 * max_val

        if len(s) == 0 :
            return sum 

        if s[0] == '-':
            isNeg = True
            s = s[1:] 
        elif s[0] == '+':
            s = s[1:]

        for chr in s:
            val = ord(chr) - ord('0')
            if not (val<=9 and val>=0):
                break 
            sum = (sum*10) + val 
        
        if isNeg:
            sum = -1 * sum

        if sum >= max_val:
            sum = max_val - 1
        elif sum < min_val:
            sum = min_val

        return sum 

        
        
# @lc code=end

