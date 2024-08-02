class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        one_count = sum(nums)
        length = len(nums)
        min_swaps = current_swaps = one_count - sum(nums[:one_count])

        for i in range(one_count, length + one_count):
            current_swaps += nums[i - one_count] - nums[i % length]
            min_swaps = min(current_swaps, min_swaps)

        return min_swaps
