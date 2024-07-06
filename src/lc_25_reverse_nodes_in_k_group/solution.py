from lc_25_reverse_nodes_in_k_group.listnode import ListNode

class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 0:
            return None
        
        res_head = ListNode(0)
        res_tail = res_head
        while head:
            first = head
            second = self._find_kth_node(head, k)
            if not second:
                res_tail.next = head
                break

            head = second.next
            second.next = None
            self._reverse(first)
            res_tail.next = second
            res_tail = first
        
        return res_head.next
    
    def _find_kth_node(self, head, k):
        while head and k > 1:
            head = head.next
            k -= 1
            
        return head
    
    def _reverse(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
            
        return prev