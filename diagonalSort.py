class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0]) 
        diagonals = defaultdict(list) 
        
        for row in range(rows): 
            for col in range(cols): 
                diagonals[row - col].append(mat[row][col])
        
        for diagonal in diagonals.values(): 
            diagonal.sort() 
        
        for row in range(rows): 
            for col in range(cols): 
                mat[row][col] = diagonals[row - col].pop(0)
        
        return mat 
