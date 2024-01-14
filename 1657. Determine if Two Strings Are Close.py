class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        freq1 = [0] * 26
        freq2 = [0] * 26

        for letter in word1:
            freq1[ord(letter) - ord('a')] += 1
        
        for letter in word2:
            freq2[ord(letter) - ord('a')] += 1

        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False
        
        freq1.sort()
        freq2.sort()

        return freq1 == freq2


#Test
word1 = "abbccc"
word2 = "bcabba"
print(Solution().closeStrings(word1, word2))