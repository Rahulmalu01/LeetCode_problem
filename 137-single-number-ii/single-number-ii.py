class Solution(object):
    def singleNumber(self, nums):
        num = len(nums)
        nums.sort()
        for i in range(0,(num-2),3):
            if nums[i] != nums[i+2]:
                return nums[i]
        return nums[num - 1]