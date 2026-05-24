class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.sorted()
        t.sorted()
        if len(s) == len(t):
            return True
        return False
        