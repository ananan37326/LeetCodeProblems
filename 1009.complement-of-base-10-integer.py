#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
import math

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        powerOfTwo = math.log2(n)
        if math.ceil(powerOfTwo) == powerOfTwo:
            powerOfTwo +=1
        else:
            powerOfTwo = math.ceil(powerOfTwo)
        
        return int(2**powerOfTwo - (n+1))
        
# @lc code=end

