class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_, max_ = arrays[0][0], arrays[0][-1]
        max_dist = 0 

        for i in range(1, len(arrays)): 
            arr = arrays[i]
            max_dist = max(max_dist, abs(arr[-1] - min_), abs(max_ - arr[0]))
            min_ = min(min_, arr[0])
            max_ = max(max_, arr[-1])
        
        return max_dist
