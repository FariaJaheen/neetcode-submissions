class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        tt = sorted(t)
        for i in range(len(ss)):
            for j in range(len(tt)):
                if ss[i] == tt[j]:
                    i += 1
                    return True
                return False
        