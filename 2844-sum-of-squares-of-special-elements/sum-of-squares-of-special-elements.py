class Solution(object):
    def sumOfSquares(self, nums):
        output = 0
        l = len(nums)
        for i in range(l):
            if l % (i+1) == 0:
                output += nums[i]**2
        return output
        