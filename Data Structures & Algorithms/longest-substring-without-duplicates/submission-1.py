class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0

        start = 0
        res = 1
        c_map = defaultdict()

        for i, c in enumerate(s):
            if c in c_map:
                old_idx = c_map[c]
                start = max(old_idx + 1, start)
                
            c_map[c] = i
            res = max(res, (i - start+1))

        return res