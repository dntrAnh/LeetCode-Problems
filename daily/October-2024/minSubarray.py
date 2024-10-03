class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum_nums = sum(nums)
        remainder = total_sum_nums % p

        if remainder == 0: 
            return 0 
        
        prefix_mod = {0: -1}
        prefix_sum = 0
        min_len = float('inf')

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            needed_mod = (prefix_sum - remainder + p) % p

            if needed_mod in prefix_mod:
                min_len = min(min_len, i - prefix_mod[needed_mod])

            prefix_mod[prefix_sum] = i

        return min_len if min_len < len(nums) else -1
