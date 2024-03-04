class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        res = score = 0
        tokens.sort()

        l, r = 0, len(tokens) - 1

        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                res = max(res, score)

            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            
            else:
                break
        
        return res
        