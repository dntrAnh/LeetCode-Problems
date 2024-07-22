class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3: 
            return 0 
        
        nums.sort() 
        result = float('inf')

        result = min(result, nums[-1] - nums[3])
        result = min(result, nums[-4] - nums[0])
        result = min(result, nums[-2] - nums[2])
        result = min(result, nums[-3] - nums[1])
        
        return result 
