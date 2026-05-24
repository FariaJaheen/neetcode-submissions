class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if nums[i] == nums[i-1]:
            return True 
        return False