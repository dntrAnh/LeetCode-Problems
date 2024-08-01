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

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF(len(edges) + 1)

        for x, y in edges:
            if uf.find(x) == uf.find(y): # cycle detection 
                return [x, y]
            uf.union(x, y)
