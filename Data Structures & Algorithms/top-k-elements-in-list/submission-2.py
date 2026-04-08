class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1

        list_num = [[k, v] for k,v in num_dict.items()]
        list_num.sort(key=lambda x:x[1], reverse=True)
        print(list_num)
        res = []
        for i in range(k):
            res.append(list_num[i][0])
        
        return res