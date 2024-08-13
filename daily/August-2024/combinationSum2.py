class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target): 
            if target == 0: 
                result.append(temp[:])
                return 
            elif target < 0: 
                return 
            for i in range(start, n): 
                if i > start and candidates[i] == candidates[i - 1]: 
                    continue 
                temp.append(candidates[i]) 
                backtrack(i + 1, target - candidates[i]) 
                temp.pop()

        candidates.sort() 
        n = len(candidates) 

        result = []
        temp = []

        backtrack(0, target) 
        return result
