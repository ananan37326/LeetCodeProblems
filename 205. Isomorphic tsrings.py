class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sTot = {}
        tTos = {}
        
        for (letter1, letter2) in zip(s, t):
           if (letter1 in sTot and sTot[letter1] != letter2) or (letter2 in tTos and tTos[letter2] != letter1):
               return False
           
           sTot[letter1] = letter2
           tTos[letter2] = letter1
            
        return True