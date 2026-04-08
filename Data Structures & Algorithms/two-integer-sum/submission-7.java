class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> num_map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int current_num = nums[i];
            int diff = target - current_num;
            boolean diff_exist = num_map.containsKey(diff);

            if (diff_exist) {
                return new int[] {num_map.get(diff), i};
            }

            num_map.put(current_num, i);
        }

        return new int[]{};
    }
}
