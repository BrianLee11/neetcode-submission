# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current_node = head
        while current_node and current_node.val == val:
            current_node = current_node.next
        new_head = current_node

        while current_node:
            next_node = current_node.next

            while next_node and next_node.val == val:
                next_node = next_node.next

            if next_node and next_node.val != val:
                current_node.next = next_node

            if not next_node:
                current_node.next = None

            current_node = current_node.next

        return new_head

        