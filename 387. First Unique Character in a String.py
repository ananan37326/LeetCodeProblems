class Solution:
    def firstUniqChar(self, s: str) -> int:
        countMap = defaultdict(int)

        for ch in s:
            countMap[ch] += 1
        
        for (i, ch) in enumerate(s):
            if countMap[ch] == 1:
                return i
        return -1
        