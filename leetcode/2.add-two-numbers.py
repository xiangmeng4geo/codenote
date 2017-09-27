# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = None
        pre = None
        plus_one = 0
        while l1 or l2 or plus_one:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            val = n1 + n2 + plus_one 
            if val > 9:
                plus_one = 1
                val -= 10
            else:
                plus_one = 0
            cur = ListNode(val)
            if first == None:
                first = cur
                pre = cur
            else:
                pre.next = cur
                pre = pre.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return first
