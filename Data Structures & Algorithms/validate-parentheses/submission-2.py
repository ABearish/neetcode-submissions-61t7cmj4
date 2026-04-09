class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        parentheses_map = { "]":"[", ")":"(", "}":"{" }
        stack = []

        for c in s:
            if c in parentheses_map:
                if len(stack) < 1: return False
                ele = stack.pop()
                if  ele != parentheses_map[c]:
                    return False            
            else:
                stack.append(c)
        return True if len(stack) == 0 else False
