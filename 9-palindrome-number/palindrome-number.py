class Solution(object):
    def isPalindrome(self, x):
        a = str(x)[::-1]
        return a == str(x)
        