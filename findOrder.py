class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        
        for prerequisite in prerequisites:
            adjList[prerequisite[0]].append(prerequisite[1])
        
        res = []
        visiting = [False] * numCourses
        visited = [False] * numCourses
        
        def dfs(curr: int) -> bool:
            if visited[curr]:
                return True
            if visiting[curr]:
                return False
            
            visiting[curr] = True
            for neighbor in adjList[curr]:
                if not dfs(neighbor):
                    return False
            visiting[curr] = False
            visited[curr] = True
            
            res.append(curr)
            
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
