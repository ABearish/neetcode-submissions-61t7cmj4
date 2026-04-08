class Solution {
    public int[] productExceptSelf(int[] nums) {
        int zeroes = 0, prod = 1;
        for (int num : nums) {
            if (num != 0) {
                prod *= num;
            } else {
                zeroes++;
            }
        }
        if (zeroes > 1) {
            return new int[nums.length];
        }
        int results[] = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (zeroes > 0) {
                results[i] = num == 0 ? prod : 0;
            } else {
                results[i] = (int)(prod/nums[i]);
            }
        }
        return results;
    }
}  
