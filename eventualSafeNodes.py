class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        num_node = len(graph)

        new_graph = {i: [] for i in range(num_node)} 
        indegree = {i: 0 for i in range(num_node)}

        for node, adj_nodes in enumerate(graph):
            for adj_node in adj_nodes:
                new_graph[adj_node].append(node)
            indegree[node] += len(adj_nodes)

        safe_nodes = []
        queue = deque()

        for node in range(num_node):
            if indegree[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)

            for adj_node in new_graph[node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
        
        safe_nodes.sort()
        return safe_nodes
