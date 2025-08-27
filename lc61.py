from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    """Helper function to print a linked list"""
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        if k == 0:
            return head
    
        # Create tmp nodes
        node = head
        while node != None:
            if node.next == None:
                tail = node

            nodes.append(node.val)
            node = node.next
        
        count = len(nodes)
        if not count or k % count == 0:
            return head
        
        first = count - k % count
        
        current = head
        for i in range(first, count):
            current.val = nodes[i]
            current = current.next

        for i in range(0, first):
            current.val = nodes[i]
            current = current.next
            
        return head



if __name__ == "__main__":
    # Example 1: [1,2,3,4,5] rotate by k=2 should become [4,5,1,2,3]
    example1 = create_linked_list([1, 2, 3, 4, 5])
    print("Example 1 - Original:")
    print_linked_list(example1)
    
    sol = Solution()
    rotated1 = sol.rotateRight(example1, 201)
    print("After rotating:")
    print_linked_list(rotated1)
    