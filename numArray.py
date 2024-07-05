class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] + list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
