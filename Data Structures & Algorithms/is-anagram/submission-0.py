class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count:[str,int] = {}
        
        for char in s:
            if not char in char_count:
                char_count[char] = 0;
            char_count[char] += 1
        
        for char in t:
            if not char in char_count:
                return False
            char_count[char] -= 1

        for key in char_count.values():
            if key != 0:
                return False

        return True