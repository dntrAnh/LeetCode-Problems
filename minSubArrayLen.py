class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf') 

        start, end = 0, 0 
        curr_sum = 0 

        while end < len(nums): 
            curr_sum += nums[end] 
            end += 1
            
            while start < end and curr_sum >= target: 
                curr_sum -= nums[start] 
                start += 1
                min_length = min(min_length, end - start + 1) 
        
        if min_length == float('inf'): 
            return 0 
        else: 
            return min_length 
