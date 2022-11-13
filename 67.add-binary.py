#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a),len(b))):
            digitA = ord(a[i]) - ord('0') if i < len(a) else 0
            digitB = ord(b[i]) - ord('0') if i < len(b) else 0

            char = str((digitA+digitB+carry)%2)
            res = char + res 
            carry = (digitA+digitB+carry) // 2
        
        if carry:
            res = "1" + res 
        return res 
        
# @lc code=end

