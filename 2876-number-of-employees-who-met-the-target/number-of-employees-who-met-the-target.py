class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        num = 0
        hours.sort()
        for i in range(len(hours)):
            if hours[i] >= target:
                return len(hours) - i
        return 0