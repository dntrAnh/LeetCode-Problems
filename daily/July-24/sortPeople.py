import heapq

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        max_heap = []

        for idx, height in enumerate(heights): 
            heapq.heappush(max_heap, (-height, idx)) 
        
        result = []
        while max_heap: 
            _, idx = heapq.heappop(max_heap) 
            result.append(names[idx]) 
        
        return result 
