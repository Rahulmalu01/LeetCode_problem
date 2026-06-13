# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def linked_list_to_num(self, head):
        num = 0
        place = 1
        while head:
            num += head.val * place
            place *= 10
            head = head.next
        return num
    def num_to_linked_list(self, num):
        dummy = ListNode(0)
        curr = dummy
        for digit in str(num)[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next
        return dummy.next
    def addTwoNumbers(self, l1, l2):
        num1 = self.linked_list_to_num(l1)
        num2 = self.linked_list_to_num(l2)
        sum = num1 + num2
        l3 = self.num_to_linked_list(sum)
        return l3
        