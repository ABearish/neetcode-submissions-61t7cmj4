class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1), len(s2)
        if n1 > n2: return False

        ## Create two empty list a-z
        s1_list = [0] * 26
        s2_list = [0] * 26

        # iterate through n1
        for i in range(n1):
            s1_list[ord(s1[i]) - ord('a')] += 1
            s2_list[ord(s2[i]) - ord('a')] += 1

        if s1_list == s2_list: return True

        for i in range(n1, n2):
            s2_list[ord(s2[i]) - ord('a')] += 1
            s2_list[ord(s2[i- n1]) - ord('a')] -= 1

            if s1_list == s2_list: return True

        return False