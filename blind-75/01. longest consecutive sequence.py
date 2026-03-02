class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_count = 0
        
        for i in nums_set:
            if i - 1 not in nums_set:
                j = i
                count = 0
                while (j in nums_set):
                    count = count + 1
                    j = j + 1
                if count > longest_count:
                    longest_count = count
        
        return longest_count
