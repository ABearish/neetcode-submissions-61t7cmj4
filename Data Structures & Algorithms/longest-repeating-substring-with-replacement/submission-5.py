class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s) 
        f_map = defaultdict(int)
        f_max = 0
        l = 0
        count = 0

        for r in range(n):
            rc = s[r]
            f_map[rc] += 1

            f_max = max(f_max, f_map[rc])

            while (r-l + 1) - f_max > k:
                f_map[s[l]] -= 1
                l += 1

        count = max(count, r-l+1)
        return count             