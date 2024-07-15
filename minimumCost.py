import heapq 

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # max_heap 
        heap = []

        for cost in horizontalCut: 
            heapq.heappush(heap, (-cost, 'h'))
        for cost in verticalCut: 
            heapq.heappush(heap, (-cost, 'v'))

        horizontal_pieces = 1
        vertical_pieces = 1
        
        total_cost = 0
        
        while heap:
            cost, direction = heapq.heappop(heap)
            cost = -cost
            
            if direction == 'h':
                total_cost += cost * vertical_pieces
                horizontal_pieces += 1
            else:
                total_cost += cost * horizontal_pieces
                vertical_pieces += 1
        
        return total_cost
