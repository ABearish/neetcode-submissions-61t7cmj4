class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for ss in s:
            if (ord(ss) > 64 and ord(ss) < 91) or (ord(ss) > 96 and ord(ss) < 123) or (ord(ss) > 47 and ord(ss) < 58):
                clean_str += ss.lower()
        
        i = 0
        j = len(clean_str) - 1
        while (i < j):
            left_char = clean_str[i]
            right_char = clean_str[j]
            i += 1
            j -= 1
            if left_char != right_char:
                return False

        return True