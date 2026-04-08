class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_list = [0] * 26

        for i, c in enumerate(s):
            code = ord(c) - ord('a')
            char_list[code] += 1
        
        for j, c in enumerate(t):
            code = ord(c) - ord('a')
            if char_list[code] <= 0:
                return False
            char_list[code] -= 1

        for freq in char_list:
            if freq != 0:
                return False
        
        return True