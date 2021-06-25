# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        
        while head and head.next:
            # b가 head를 가리킴
            b = head.next
            head.next = b.next
            b.next = head
            
            # prev가 b를 가리킴
            prev.next = b
            
            head = head.next
            prev = prev.next.next
            
        return root.next