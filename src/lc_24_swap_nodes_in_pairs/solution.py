from lc_24_swap_nodes_in_pairs.listnode import ListNode

class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        
        res_head = ListNode(0)
        res_tail = res_head
        while head:
            first = head
            second = first.next
            
            if second is not None:
                head = second.next
                
                second.next = first
                first.next = None
                
                res_tail.next = second
                res_tail = first
            else:
                head = None
                
                res_tail.next = first
                res_tail = first
                
        return res_head.next
