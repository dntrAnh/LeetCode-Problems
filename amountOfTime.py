# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        def build_graph(node): 
            nonlocal graph
            if node.left: 
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                build_graph(node.left)
            if node.right: 
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                build_graph(node.right)
        
        build_graph(root)

        queue = deque([start])
        visited = set() 
        visited.add(start)

        minute = -1
        while queue: 
            for _ in range(len(queue)): 
                node = queue.popleft() 
                for nbr in graph[node]: 
                    if nbr not in visited: 
                        queue.append(nbr)
                        visited.add(nbr)
            minute += 1
        
        return minute 
