"""
LeetCode problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
Description: Given a linked list, remove the n-th node from the end of list and return its head.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        temp2 = head
        counter = 1

        # determine length of the list
        while temp.next is not None:
            temp = temp.next
            counter = counter + 1

        # special case, list only has 1 element or removing the head node
        if (head.next is None) or (n == counter):
            temp2 = head.next
            head = temp2
            return head

        # general case
        for i in range(1, counter - n):
            temp2 = temp2.next
        temp = temp2.next
        temp2.next = temp.next
        return head
