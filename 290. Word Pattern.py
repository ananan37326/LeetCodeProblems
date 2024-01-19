class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w_to_p = {}
        words = s.split(' ')
        
        if len(pattern) != len(words):
            return False
        
        if len(set(pattern)) != len(set(words)):
            return False
        
        for (word,p) in zip(words,pattern):
            if word in w_to_p and w_to_p[word] != p:
                return False
            
            w_to_p[word] = p
            
        return True
    
#test
sol = Solution()
print(sol.wordPattern("abba","dog cat cat fish"))