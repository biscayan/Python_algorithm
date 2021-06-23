# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        
        carry = 0
        
        while l1 or l2 or carry:
            num_sum = 0
            
            if l1:
                num_sum += l1.val
                l1 = l1.next
                
            if l2:
                num_sum += l2.val
                l2 = l2.next
                
            # 자리올림수와 값 계산
            carry, val = divmod(num_sum+carry, 10)
            head.next = ListNode(val)
            head = head.next
            
        return root.next