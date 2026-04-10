class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        # Edge Case: s2 cannot be longer than s1
        if n2 < n1: return False
        # Store pattern in an array
        s1_list = [0] * 26
        for i, c in enumerate(s1):
            idx = ord(c) - 97
            s1_list[idx] += 1
        # We create a variblea to track the left window
        l = 0
        r = 1
        while l < n2:
            # Copy list for testing
            t_list = list(s1_list)
            s1_idx = 0
    
            # iterate until we find the start of the pattern
            while l < n2-1 and s1_list[ord(s2[l]) - 97] == 0:
                l += 1 

            # decrement the freq in list
            if t_list[ord(s2[l]) - 97] == 0:
                return False
           
            t_list[ord(s2[l]) - 97] -= 1
            s1_idx += 1
            # move the right one idx over to start our window search
            r = l + 1
            while r < n2 and t_list[ord(s2[r]) - ord('a')] > 0:
                t_list[ord(s2[r]) - 97] -= 1
                s1_idx += 1
                r += 1
            
            if s1_idx == n1:
                return True
            else: 
                l += 1
        return False