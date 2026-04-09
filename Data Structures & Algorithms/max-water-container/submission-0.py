class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n < 1: return 0
        maximum_amount = 0
        l,r = 0, n -1
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            a = w*h
            maximum_amount = max(maximum_amount, a)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maximum_amount
