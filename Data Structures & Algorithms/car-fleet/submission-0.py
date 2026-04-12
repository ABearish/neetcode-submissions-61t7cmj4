class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## Sort desc position
        cars = sorted(zip(position, speed), reverse=True)
        ## Crate a stack
        stack = []
        ## iterate with pointers on both list
        for p,s in cars:
            ## calculate how long it would take them to reach finishline
            t = (target - p) / s
            ## add to the stack if the current position is greater than the stack
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)