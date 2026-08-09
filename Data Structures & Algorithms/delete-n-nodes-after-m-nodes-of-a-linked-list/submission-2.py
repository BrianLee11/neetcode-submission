# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        target_include = m  # m
        target_pass = n  # n

        count_include = 0
        count_pass = 0
        current = head

        while current:
            while count_include < target_include - 1:
                if current.next: 
                    current = current.next
                    count_include += 1
                else:
                    break

            if current:
                previous_node = current
                next_node = current

                while next_node and (count_pass <= target_pass):
                    next_node = next_node.next
                    count_pass += 1

                previous_node.next = next_node
                current = next_node

                count_include = 0
                count_pass = 0
            else:
                break

        return head