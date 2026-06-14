class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if stack and ord(i) - ord(stack[-1]) in (1, 2):
                stack.pop()
            else:
                stack.append(i)
        if not stack:
            return True
        return False