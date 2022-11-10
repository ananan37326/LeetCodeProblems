#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        for val in collections.Counter(s).values():
            result += val//2 * 2

        return min(result+1, len(s))
        
# @lc code=end

