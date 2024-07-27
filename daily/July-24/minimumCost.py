# Floyd-Warshall's Algorithm
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[float('inf')] * 26 for _ in range(26)]

        for i in range(26): 
            graph[i][i] = 0
        
        for idx in range(len(original)): 
            src = ord(original[idx]) - ord('a')
            trg = ord(changed[idx]) - ord('a')
            new_cost = cost[idx] 
            graph[src][trg] = min(graph[src][trg], new_cost)
        
        for k in range(26): 
            for i in range(26): 
                for j in range(26): 
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        total_cost = 0 
        for i in range(len(source)): 
            src = ord(source[i]) - ord('a') 
            trg = ord(target[i]) - ord('a') 
            new_cost = graph[src][trg]
            total_cost += new_cost 
        
        return total_cost if total_cost < float('inf') else -1 
