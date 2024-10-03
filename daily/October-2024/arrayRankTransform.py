import heapq 

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        heap = []
        
        for idx, num in enumerate(arr):
            heapq.heappush(heap, (num, idx))
        
        result = [0] * len(arr)
        curr_rank = 0
        prev_num = None
        
        while heap:
            num, idx = heapq.heappop(heap)
            if num != prev_num: 
                curr_rank += 1
            result[idx] = curr_rank
            prev_num = num
        
        return result
