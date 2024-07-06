from lc_23_merge_k_sorted_lists.listnode import ListNode
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists):
        pq = PriorityQueue()
        for head in lists:
            if head:
                pq.put((head.val, head))
                
        merged_head = ListNode(-1)
        merged_tail = merged_head
        while not pq.empty():
            node = pq.get()[1]
            merged_tail.next = node
            merged_tail = merged_tail.next
            
            node = node.next
            merged_tail.next = None
            
            if node:
                pq.put((node.val, node))
                
        return merged_head.next
