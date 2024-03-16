# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has
# Node.val == val, and return the new head.


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        while head and head.val == val:
            head = head.next
        return head
