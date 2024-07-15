class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        cooking_graph = defaultdict(list)
        indegree = defaultdict(int)

        for idx, recipe in enumerate(recipes): 
            ingredient = ingredients[idx]
            for ing in ingredient: 
                cooking_graph[ing].append(recipe)
                indegree[recipe] += 1
        
        queue = deque(supplies)
        result = []

        while queue: 
            ing = queue.popleft() 
            for recipe in cooking_graph[ing]: 
                indegree[recipe] -= 1
                if indegree[recipe] == 0: 
                    queue.append(recipe)
                    result.append(recipe)
        
        return result 
