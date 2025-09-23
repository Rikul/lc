from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        node = head
        less_than_x = []
        eq_or_greater = []

        while node:
            if node.val < x:
                less_than_x.append(node.val)
            else:
                eq_or_greater.append(node.val)            
            node = node.next

        node = head
        for n in less_than_x:
            node.val = n
            node = node.next

        for n in eq_or_greater:
            node.val = n
            node = node.next


        return head