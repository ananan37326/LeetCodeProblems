class Solution:
    # Given a string s, find the length of the longest substring without repeating characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_length = 1
        start = 0
        end = 1
        while end < len(s):
            if s[end] not in s[start:end]:
                end += 1
            else:
                start += 1
            max_length = max(max_length, end - start)
        return max_length


# Test
s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))