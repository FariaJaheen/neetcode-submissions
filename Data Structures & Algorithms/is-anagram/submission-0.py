class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.sort()
        t.sort()
        if len(s) == len(t):
            return True
        return False
        