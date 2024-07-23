class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_map = Counter(nums) 
        return sorted(nums, key = lambda num : (freq_map[num], -num))
