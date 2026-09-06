class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            curr_hours = sum(math.ceil(p/mid) for p in piles)

            if curr_hours <= h:
                high = mid
            else:
                low = mid + 1

        return low