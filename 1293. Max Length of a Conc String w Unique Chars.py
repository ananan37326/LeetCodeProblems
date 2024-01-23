class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set() 

        def overlap(s, charSet):
            occur = set()

            for c in s:
                if c in charSet or c in occur:
                    return True
                occur.add(c)
            
            return False

        def backtrack(i):
            if i == len(arr):
                return len(charSet)

            res = 0
            if not overlap(arr[i], charSet):
                for c in arr[i]:
                    charSet.add(c)
                
                res = backtrack(i+1)
                for c in arr[i]:
                    charSet.remove(c)
                
            return max(res, backtrack(i+1))

        
        return backtrack(0)