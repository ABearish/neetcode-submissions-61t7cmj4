class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        if n < 1: return 0

        operator_set = set({"+", "-", "*", "/"})

        num_stack = []

        for t in tokens:
            if t in operator_set:
                num_2 = num_stack.pop()
                num_1 = num_stack.pop()
                if t == "+":
                    num_stack.append(num_1 + num_2)
                elif t == "-":
                    num_stack.append(num_1 - num_2)
                elif t == "*":
                    num_stack.append(num_1 * num_2)
                elif t == "/":
                    num_stack.append(int(num_1 / num_2))
            else:
                num_stack.append(int(t))
        return num_stack.pop()