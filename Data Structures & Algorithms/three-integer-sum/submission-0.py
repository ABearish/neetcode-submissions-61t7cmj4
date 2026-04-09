class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        res = []
        for i in range(n - 2):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i+1, n -1
            while l < r:
                curr = a + nums[l] + nums[r]
                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1

        return res