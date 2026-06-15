class Solution(object):
    def moveZeroes(self, nums):
        left = 0 
        length = len(nums)
        for right in range(length):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums
        