import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = Counter(s) 

        heap = []
        for char, freq in freq_map.items(): 
            heapq.heappush(heap, (-freq, char))
        
        prev = None 
        result = ""

        while heap or prev: 
            if prev and not heap: 
                return ""
            freq, char = heapq.heappop(heap) 
            freq += 1
            result += char 
            if prev: 
                heapq.heappush(heap, prev) 
                prev = None 
            if freq: 
                prev = (freq, char)

        return result 
