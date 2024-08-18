import heapq 

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2, 3, 5]
        heap = [1]
        visited = set()
        visited.add(1)

        for _ in range(n): 
            curr = heapq.heappop(heap)
            for prime in primes: 
                new_num = curr * prime 
                if new_num not in visited: 
                    heapq.heappush(heap, new_num)
                    visited.add(new_num)
        
        return curr
