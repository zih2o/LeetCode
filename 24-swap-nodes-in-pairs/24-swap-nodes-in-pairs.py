# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head and head.next:
            node = head.next
            head.next = self.swapPairs(node.next)
            node.next = head
            return node
        return head