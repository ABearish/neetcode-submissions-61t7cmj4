class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c_map = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
                
            c_map[tuple(count)].append(s)
    
        return list(c_map.values())