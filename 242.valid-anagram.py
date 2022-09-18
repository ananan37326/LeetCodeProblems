#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        for letter in s:
            try:
                dict_s[letter] += 1
            except:
                dict_s[letter] = 1
        dict_t = {}
        for letter in t:
            try:
                dict_t[letter] += 1
            except:
                dict_t[letter] =1
        
        if dict_s == dict_t:
            return True
        return False 
        
# @lc code=end

