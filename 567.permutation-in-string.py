#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # declaring variables
        l = 0 # left pointer
        char_count = {} # dictionary to keep count of the characters of the pattern
        matched = 0 # number of matched character

        # update the dictionary
        for chr in s1:
            char_count[chr] = 1 + char_count.get(chr, 0)

        # looping through the string with right pointer
        for r in range(len(s2)):
            r_char = s2[r] # character at the righ of the window

            # check if the character is in the pattern
            # if yes, decrement that character count by 1, if the count is 0 then we get one match
            # if the number of match is same as pattern length, we return True
            if r_char in char_count:
                char_count[r_char] -= 1

                if char_count[r_char] == 0:
                    matched += 1
            
            if matched == len(char_count):
                return True

            # check if the window size is larger than the length of the pattern
            while (r-l+1) > len(s1)-1:
                l_char = s2[l]
                if l_char in char_count:
                    if char_count[l_char]==0:
                        matched -= 1
                    char_count[l_char] += 1
                l += 1
            
        return False 
        
        
# @lc code=end

