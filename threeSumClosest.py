class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        n = len(nums) 
        diff = float('inf') 

        for i in range(n - 1): 
            start, end = i + 1, n - 1
            while start < end: 
                curr_sum = nums[i] + nums[start] + nums[end]
                if curr_sum == target: 
                    return target 
                elif abs(target - curr_sum) < diff: 
                    diff = abs(target - curr_sum)
                    result = curr_sum 

                if curr_sum > target: 
                    end -= 1
                else: 
                    start += 1
        
        return result 
