class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)): 
            if j < 2 or nums[i] != nums[j - 2]: 
                nums[j] = nums[i] 
                j += 1
        
        return j
