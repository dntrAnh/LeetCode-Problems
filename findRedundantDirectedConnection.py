class UF:
    def __init__(self, n):
        self.parents = {i: i for i in range(n)}
        self.size = {i: 1 for i in range(n)}
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                self.parents[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parents[rootY] = rootX
                self.size[rootX] += self.size[rootY]
        else: 
            return False 
        
        return True 

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UF(n + 1)
        parent = list(range(n + 1))

        candidate1 = candidate2 = None
        for u, v in edges:
            if parent[v] != v:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
                break
            parent[v] = u

        uf = UF(n + 1)
        for u, v in edges:
            if [u, v] == candidate2:
                continue
            if not uf.union(u, v):
                if candidate1:
                    return candidate1
                return [u, v]
        
        return candidate2
