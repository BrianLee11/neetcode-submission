# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def findLeftRightNode(head):
            slow_head = head
            previous_slow_head = None
            fast_head = head
            left_node = None
            right_node = None

            while fast_head.next:
                previous_slow_head = slow_head
                slow_head = slow_head.next
                left_node = previous_slow_head

                if fast_head.next.next:
                    fast_head = fast_head.next.next
                    right_node = slow_head.next
                else:
                    right_node = left_node.next
                    break
            
            return left_node, right_node

        def reverseDirection(head, final_node):
            previous_node = None
            current_node = head

            while previous_node is not final_node:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node

            return head


        left_node, right_node = findLeftRightNode(head)
        reverseDirection(head, left_node)

        while (left_node and right_node):
            if (left_node.val != right_node.val):
                return False
            left_node = left_node.next
            right_node = right_node.next

        return True
        