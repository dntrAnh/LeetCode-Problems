class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for element in popped: 
            while j < len(pushed) and (len(stack) == 0 or element != stack[-1]): 
                stack.append(pushed[j])
                j += 1
            if stack[-1] != element: 
                return False
            else: 
                stack.pop() 
        return len(stack) == 0
