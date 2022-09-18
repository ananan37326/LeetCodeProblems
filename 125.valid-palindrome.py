#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = ""
        for character in s:
            if character.isalnum():
                converted += character.lower()
        
        left,right = 0, len(converted)-1

        while left <=right:
            if converted[left] != converted[right]:
                return False 
            left += 1
            right -= 1
        return True 
        
# @lc code=end

