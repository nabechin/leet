class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast_pointer = head
        slow_pointer = head
        while(fast_pointer):
            if fast_pointer.next is None:
                return slow_pointer
            if fast_pointer.next.next is None:
                return slow_pointer.next
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
