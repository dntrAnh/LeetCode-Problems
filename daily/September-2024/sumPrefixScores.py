class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.score = 0
    
    def add(self, s: str, n: int): 
        if n: 
            self.score += 1

        if n == len(s): 
            return 

        if s[n] not in self.children: 
            self.children[s[n]] = TrieNode()

        self.children[s[n]].add(s, n + 1)
    
    def traverse(self, s: str, n: int): 
        if n == len(s): 
            return self.score
            
        return self.score + self.children[s[n]].traverse(s, n + 1)


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = TrieNode() 

        for word in words: 
            trie.add(word, 0)

        result = []

        for word in words: 
            result.append(trie.traverse(word, 0))

        return result
