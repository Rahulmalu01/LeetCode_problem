class Solution(object):
    def twoSum(self, num, target):
        seen = {}
        for index, value in enumerate(num):
            complement = target - value
            if complement in seen:
                return (seen[complement], index)
            seen[value] = index
        return None
        