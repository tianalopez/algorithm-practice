# Given the head of a singly linked list,
# reverse the list, and return the reversed list.


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node

            prev_node = current_node
            current_node = next_node

        return prev_node

class Solution:
    pass
