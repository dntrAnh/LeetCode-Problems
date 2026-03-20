# House Robber II

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(houses):
            dp = [0] * len(houses)
            dp[0] = houses[0]

            for i in range(len(houses)):
                take = houses[i] + (dp[i-2] if i > 1 else 0)
                skip = dp[i-1]
                dp[i] = max(take, skip)
            
            return dp[-1]
        
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
