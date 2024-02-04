class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = defaultdict(int), defaultdict(int)

        for ch in t:
            countT[ch] += 1

        INF = 999999
        res, resLen = [-1,-1], INF
        have, need = 0, len(countT)

        l = 0
        for r in range(len(s)):
            cur = s[r]
            window[cur] += 1

            if cur in countT and window[cur] == countT[cur]:
                have += 1
            
            while have == need:
                curMin = r - l + 1

                if curMin < resLen:
                    resLen = curMin
                    res = [l, r]
                
                leftChar = s[l]

                window[leftChar] -= 1

                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    have -= 1
                
                l += 1
            
        resLeft, resRight = res
        return s[resLeft: resRight + 1] if resLen < INF else ""
        