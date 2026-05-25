class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = sorted(strs)
        if len(strs) != len(new_strs):
            return None
        