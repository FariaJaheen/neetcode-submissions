class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        tt = sorted(t)
        for i, j in range(len(ss)):
            if ss[i] == tt[j]:
                return True
        return False
        