class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        length = 0
        for i in s:
            if i in sub:
                parts = sub.split(i, 1)
                sub = parts[1] if len(parts) > 1 else sub
            sub = sub + i
            if len(sub) > length:
                length = len(sub)

        return length
