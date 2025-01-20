from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = []

        current = head
        previous = None
        while current:
            lst.append((previous,current))
            previous = current
            current = current.next

        previous, node = lst[-n]
        if previous == None:
            return node.next
        else:
            previous.next = node.next
            
        return head
