class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq_map = Counter(nums1)
        result = []
        for i in nums2:
            if i in freq_map and freq_map[i] > 0:
                result.append(i)
                freq_map[i] -= 1
        return result
