class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1;
        num_zeros = 0
        for num in nums:
            if (num == 0):
                num_zeros += 1
            else:
                prod *= num

        if (num_zeros > 1):
            return [(x*0) for x in range(0, len(nums))]

        results = [0] * len(nums)

        for i, c in enumerate(nums):
            if num_zeros: results[i] = 0 if c else prod
            else: results[i] = int(prod//nums[i])

        return results