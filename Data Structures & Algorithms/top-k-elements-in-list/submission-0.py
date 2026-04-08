from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        # sort by freq
        sorted_freq = list(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        results = [];
        for i in range(0, k):
            current_ele = sorted_freq[i][0]
            results.append(current_ele)
        return sorted(results);