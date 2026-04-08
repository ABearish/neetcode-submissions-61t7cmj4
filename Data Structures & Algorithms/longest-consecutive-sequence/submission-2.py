class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        num_set = set(nums)
        
        count = 1
        max_count = 1
        nums.sort()
        num_check = nums[0]
        i = 0
        while i < len(nums) - 1:
            curr = nums[i]
            if (num_check + 1) in num_set:
                num_check += 1
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
                num_check = nums[i+1]
                i += 1
        max_count = max(count, max_count)
        return max_count