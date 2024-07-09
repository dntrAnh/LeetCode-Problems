class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        seen = set(startGene)

        while queue: 
            gene, steps = queue.popleft() 
            if gene == endGene: 
                return steps 
            
            for i in range(len(gene)):  
                for ch in "ACGT": 
                    if gene[i] != ch: 
                        nbr = list(gene) 
                        nbr[i] = ch 
                        nbr_str = ''.join(nbr) 
                        if nbr_str not in seen and nbr_str in bank:
                            queue.append((nbr_str, steps + 1))
                            seen.add(nbr_str) 
        return -1
