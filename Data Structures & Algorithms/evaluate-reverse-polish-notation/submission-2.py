class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        if n < 1: return 0

        operator_set = set()
        operator_set.add("+")
        operator_set.add("-")
        operator_set.add("*")
        operator_set.add("/")

        num_stack = []

        for t in tokens:
            if  t.isnumeric():
                num_stack.append(int(t))
                continue
            elif len(t) > 1 and t[1:].isnumeric():
                num_stack.append(int(t))
                continue

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
        return num_stack.pop()