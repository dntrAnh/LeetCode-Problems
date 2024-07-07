class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, target): 
            if len(temp) == k and target == 0: 
                combinations.append(temp[:]) 
                return 
            elif len(temp) > k or target < 0: 
                return 
            for i in range(start, 10): 
                temp.append(i) 
                backtrack(i + 1, target - i)
                temp.pop()
        combinations = []
        temp = []
        backtrack(1, n)
        return combinations
