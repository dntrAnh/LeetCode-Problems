class UF:
    def __init__(self, n):
        self.parents = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        root_X = self.find(x)
        root_Y = self.find(y)
        if root_X == root_Y:
            return
        if self.size[root_X] < self.size[root_Y]:
            self.parents[root_X] = root_Y
            self.size[root_Y] += self.size[root_X]
        else:
            self.parents[root_Y] = root_X
            self.size[root_X] += self.size[root_Y]

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        count = 0
        uf = UF(n)
        
        for i in range(0, n, 2):
            uf.union(i, i + 1)
        
        for i in range(0, n, 2):
            left = uf.find(row[i])
            right = uf.find(row[i + 1])
            if left != right:
                uf.union(left, right)
                count += 1
        
        return count
