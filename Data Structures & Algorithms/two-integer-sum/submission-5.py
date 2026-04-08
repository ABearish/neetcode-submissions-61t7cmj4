import math
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux_nums = {}
        for idx, num in enumerate(nums):
            if not num in aux_nums:
                aux_nums[num] = []
            aux_nums[num].append(idx)
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1

        while (left <= right):
            left_num = nums[left]
            right_num = nums[right]
            currentSum = left_num + right_num
            if currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
            else: 
                temp = aux_nums[left_num].pop()
                left = temp
                temp = aux_nums[right_num].pop()
                right = temp
                return sorted([left, right])

        return []