class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        tt = sorted(t)
        for i in range(len(ss)):
            if ss[i] == tt[i]:
                return True
            return False
        