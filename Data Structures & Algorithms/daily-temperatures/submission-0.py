class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n < 2: return [0]
        stack = []
        res = [0] * n

        for i, t in enumerate(temperatures):          
                while len(stack) > 0 and temperatures[stack[len(stack) - 1]] < t:
                    temp = stack.pop()
                    res[temp] = i - temp
                    
                stack.append(i)

        return res