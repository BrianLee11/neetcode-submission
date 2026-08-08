# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA = headA
        listB = headB 

        if listA == listB:
            return listA

        set_node_listA = set()
        set_node_listB = set()

        while (listA.next and listB) or (listA and listB.next):
            if listA in set_node_listB:
                return listA
            else:
                set_node_listA.add(listA)
            
            if listB in set_node_listA:
                return listB
            else:
                set_node_listB.add(listB)

            if listA.next:
                listA = listA.next
            
            if listB.next:
                listB = listB.next   

            if (not listA.next) and (not listB.next):
                if listA in set_node_listB:
                    return listA
                if listB in set_node_listA:
                    return listB
                    
        return None        
