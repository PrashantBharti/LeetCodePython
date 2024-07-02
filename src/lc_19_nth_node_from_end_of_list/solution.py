from lc_19_nth_node_from_end_of_list.listnode import ListNode

class Solution:
    def removeNthFromEnd(self, head, n):
        if not head:
            return None
        
        len = 0
        cur = head
        while cur:
            len += 1
            cur = cur.next
            
        idx = len - n + 1
        if idx <= 0 or idx > len:
            return head
        
        if idx == 1:
            cur = head.next
            head.next = None
            head = cur
        else:
            cur = head
            while idx > 2:
                cur = cur.next
                idx -= 1

            temp = cur.next
            cur.next = temp.next
            temp.next = None
            
        return head
