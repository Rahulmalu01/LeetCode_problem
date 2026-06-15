class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        sub = arr[0] - arr[1]
        for i in range(1, len(arr)-1):
            if arr[i] - arr[i+1] != sub:
                return False
        return True
        