class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        top_k = 0
        for num in nums:
            num_dict[num] += 1
            top_k = max(top_k, num_dict[num])
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, f in num_dict.items():
            buckets[f].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)

            if len(res) == k:
                break
            
        return res