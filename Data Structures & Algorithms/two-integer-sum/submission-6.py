class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        left = 0
        right = len(nums) - 1

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        return []