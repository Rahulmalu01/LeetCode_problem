class Solution(object):
    def pivotInteger(self, n):
        sum1 = n * (n+1) // 2
        sum_l = 0
        for x in range(1, n+1):
            sum_l += x
            sum_r = sum1 - sum_l + x
            if sum_l == sum_r:
                return x
        return -1
        