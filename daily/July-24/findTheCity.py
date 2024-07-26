# Dijkstra's solution 

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list) 

        for src, dst, weight in edges: 
            graph[src].append((weight, dst))
            graph[dst].append((weight, src))

        min_idx, min_count = -1, float('inf')

        for i in range(n): 
            dist = [float('inf')] * n 
            dist[i] = 0 

            queue = [(0, i)]
            while queue: 
                weight, idx = heapq.heappop(queue)
                for nbr_weight, nbr_idx in graph[idx]: 
                    new_weight = weight + nbr_weight 
                    if new_weight < dist[nbr_idx] and new_weight <= distanceThreshold: 
                        dist[nbr_idx] = new_weight 
                        heapq.heappush(queue, (new_weight, nbr_idx))
            
            count = sum(d < float('inf') for d in dist)
            if count <= min_count:
                min_count = count
                min_idx = i

        return min_idx
