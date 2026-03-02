class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left = left - 1
                right = right + 1
            return s[left+1:right]

        for i in range(len(s)):
            p1 = expand(i, i)
            if len(p1) > len(longest):
                longest = p1
            
            p2 = expand(i, i+1)
            if len(p2) > len(longest):
                longest = p2
        
        return longest
        
