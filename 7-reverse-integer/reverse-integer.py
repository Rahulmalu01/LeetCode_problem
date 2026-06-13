class Solution(object):
    def reverse(self, x):
        mult = 1
        if x < 0:
            mult = -1
        a = int(str(abs(x))[::-1])
        if a > (2**31 - 1):
            return 0
        else :
            return a * mult