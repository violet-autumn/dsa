class Solution:
    def retunIndex(self, nums: List[int], num1: int, num2: int) -> List[int]:
        i = 0
        index1 = 0
        index2 = 0
        for number in nums:
            if number == num1:
                index1 = i
            i = i + 1
        
        i = 0
        for number in nums:
            if number == num2 and i != index1:
                index2 = i
            i = i + 1
        return [index1, index2]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_nums = set(nums)
        for i in set_nums:
            if target-i in set_nums:
                if i != (target - i) or (i == (target - i) and nums.count(i) >= 2):
                    print (i)
                    print(target-i)
                    return self.retunIndex(nums, i, target-i)
        
