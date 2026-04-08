class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let prod = 1, zeroes = 0;
        for (const num of nums) {
            if (num === 0) {
                zeroes++;
            } else {
                prod *= num;
            }
        }
        if (zeroes > 1) {
            return new Array(nums.length).fill(0);
        }
        const results = new Array(nums.length);
        let i = 0;
        for (const num of nums) {
            if (zeroes > 0) {
                results[i++] = (num === 0) ? prod : 0;
            } else {
                results[i++] = (prod/num);
            }
        }

        return results;

    }
}
