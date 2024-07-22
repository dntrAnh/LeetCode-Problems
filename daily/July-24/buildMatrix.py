class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo(conditions: List[List[int]]): 
            graph = defaultdict(list)
            indegree = defaultdict(int) 

            for a, b in conditions: 
                graph[a].append(b)
                indegree[b] += 1
            
            queue = deque() 
            for i in range(1, k + 1):
                if indegree[i] == 0: 
                    queue.append(i) 

            idx = 0 
            result = {}

            while queue: 
                node = queue.popleft() 
                result[node] = idx 
                idx += 1

                for nbr in graph[node]: 
                    indegree[nbr] -= 1
                    if indegree[nbr] == 0: 
                        queue.append(nbr) 
            return result if len(result) == k else []

        row_indices = topo(rowConditions)
        col_indices = topo(colConditions) 

        if not row_indices or not col_indices: 
            return []

        matrix = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            row = row_indices[i]
            col = col_indices[i]
            matrix[row][col] = i
        return matrix
