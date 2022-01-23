# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l: Deque = collections.deque()
        
        if not head:
            return True
        
        node = head
        
        while node is not None:
            l.append(node.val)
            node = node.next
            
        while len(l) > 1:
            if l.popleft() != l.pop():
                return False
        
        return True