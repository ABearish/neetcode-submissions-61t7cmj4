class Solution:
    import re

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for line in strs:
            size = len(line)
            encoded_str += f"{size}#{line}"
        return encoded_str
    def decode(self, s: str) -> List[str]:
        results = []
        i = 0
        k = len(s)
        while (i < k):
            j = s.find("#", i)
            length = int(s[i:j])
            start = j + 1
            end = start + length
            results.append(s[start:end])
            i = end
                
        return results


