class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        tt = sorted(t)
        
        if len(ss) != len (tt):
            return False
        return True 
        