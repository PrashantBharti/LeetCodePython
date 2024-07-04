class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        merged_head = None
        merged_tail = None
        while list1 and list2:
            if list1.val < list2.val:
                if not merged_head:
                    merged_head = list1
                    merged_tail = merged_head
                else:
                    merged_tail.next = list1
                    merged_tail = merged_tail.next
                list1 = list1.next
                merged_tail.next = None
            elif list2.val < list1.val:
                if not merged_head:
                    merged_head = list2
                    merged_tail = merged_head
                else:
                    merged_tail.next = list2
                    merged_tail = merged_tail.next
                list2 = list2.next
                merged_tail.next = None
            else:
                if not merged_head:
                    merged_head = list1
                    merged_tail = merged_head
                else:
                    merged_tail.next = list1
                    merged_tail = merged_tail.next
                    
                list1 = list1.next
                merged_tail.next = list2
                list2 = list2.next
                merged_tail = merged_tail.next
                merged_tail.next = None
                
        if list1:
            merged_tail.next = list1
        else:
            merged_tail.next = list2
        
        return merged_head
    