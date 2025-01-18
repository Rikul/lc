
import heapq
import typing
from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        h = []

        for lst in lists:
            while lst:
                heapq.heappush(h,lst.val)
                lst = lst.next

        r = None
        current = None
        for i in range(len(h)):
            new_node = ListNode(val=heapq.heappop(h), next=None)
            if not r: 
                r = new_node
                current = new_node
            else:
                current.next = new_node
                current = new_node

        return r
    

"""
# Create list1: 1->4->5
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

# Create list2: 1->3->4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Create list3: 2->6
list3 = ListNode(2)
list3.next = ListNode(6)

# Create Solution instance and merge lists
solution = Solution()
result = solution.mergeKLists([list1, list2, list3])

def print_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    return '->'.join(result)

# Print result
print("Merged list:", print_list(result))
"""