class Solution(object):
    def findMedianSortedArrays(self, num1, num2):
        new = num1 + num2
        new.sort()
        l = len(new)
        if len(new) % 2 == 0:
            a = (new[l // 2] + new[(l // 2) - 1]) / 2.0
            return a
        else:
            return new[(l - 1)/2]
        
        