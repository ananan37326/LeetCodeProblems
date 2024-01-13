class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {}
        t_dict = {}

        same_count = 0

        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1

        for i in range(len(t)):
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        for key in s_dict:
            if key in t_dict:
                same_count += min(s_dict[key], t_dict[key])

        return len(s) - same_count

#Test
s = "bab"
t = "bba"
print(Solution().minSteps(s, t))