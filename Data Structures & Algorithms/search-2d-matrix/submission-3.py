class Solution:
    def binary_search(self,nums:list, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            curr = nums[mid]
            if curr < target:
                left = mid + 1
            elif curr > target:
                right = mid - 1
            else:
                return mid
        return -1
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            left, right = 0, len(matrix[row]) - 1
            is_target_in_row = (matrix[row][left] <= target) and (matrix[row][right] >= target)
            if is_target_in_row:
                result = self.binary_search(matrix[row], target)
                if result > -1:
                    return True
                else:
                     return False
        return False

