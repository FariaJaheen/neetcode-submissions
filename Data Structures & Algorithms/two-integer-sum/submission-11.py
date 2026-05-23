class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in enumerate(nums):
          nums[i] + nums[j] == target and i != j 
        print(nums[i],nums[j])
        
        