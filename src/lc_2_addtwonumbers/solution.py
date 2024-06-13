from lc_2_addtwonumbers.listnode import ListNode

class Solution:
    def __init__(self):
        pass
    
    def addTwoNumbers(self, l1, l2):
        ansHead = None
        ansTail = None
        
        carry = 0
        while( (l1 is not None) or (l2 is not None )):
            sum = carry
            if( l1 is not None ):
                sum += l1.val
                l1 = l1.next
            if( l2 is not None ):
                sum += l2.val
                l2 = l2.next
                
            carry = sum // 10
            sum = sum % 10
            
            if ( ansHead is None ):
                ansHead = ListNode(sum)
                ansTail = ansHead
            else:
                ansTail.next = ListNode(sum)
                ansTail = ansTail.next
                
        if ( carry != 0 ):
            ansTail.next = ListNode(carry)
        
        return ansHead
