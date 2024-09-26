class TrieNode:
    ALPHABET_SIZE = 10

    def __init__(self):
        self.children = [None] * self.ALPHABET_SIZE
        self.end_char = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for c in word:
            index = int(c)
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.end_char = True

    def longest_prefix(self, word: str) -> int:
        count = 0
        curr = self.root
        for c in word:
            index = int(c)
            if curr.children[index] is None:
                break
            count += 1
            curr = curr.children[index]
        return count


class Solution:
    def __init__(self):
        self.trie = Trie()

    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        for num in arr1:
            self.trie.insert(str(num))

        max_prefix = float('-inf')
        for num in arr2:
            max_prefix = max(max_prefix, self.trie.longest_prefix(str(num)))

        return 0 if max_prefix == float('-inf') else max_prefix
