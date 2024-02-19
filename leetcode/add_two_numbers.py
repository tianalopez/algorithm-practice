# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#!Difficulty: Medium


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # new empty linked list
        new = ListNode(0)
        tail = new
        # when addition is greater than 9
        extra = 0

        while l1 is not None or l2 is not None or extra != 0:
            if l1 is not None:
                num1 = l1.val
            else:
                num1 = 0
            if l2 is not None:
                num2 = l2.val
            else:
                num2 = 0

            sum = num1 + num2 + extra
            value = sum % 10
            extra = sum // 10

            newNode = ListNode(value)
            tail.next = newNode
            tail = tail.next

            if l1 is not None:
                l1 = l1.next
            else:
                None
            if l2 is not None:
                l2 = l2.next

        answer = new.next
        new.next = None
        return answer
