class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([(1, 1)])
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        dist1[1] = 0

        while queue:
            node, freq = queue.popleft()
            curr_time = dist1[node] if freq == 1 else dist2[node]

            if (curr_time // change) % 2:
                curr_time = change * (curr_time // change + 1) + time
            else:
                curr_time += time

            for nbr in graph[node]:
                if dist1[nbr] == -1:
                    dist1[nbr] = curr_time
                    queue.append((nbr, 1))
                elif dist2[nbr] == -1 and dist1[nbr] != curr_time:
                    if nbr == n:
                        return curr_time
                    dist2[nbr] = curr_time
                    queue.append((nbr, 2))

        return 0
