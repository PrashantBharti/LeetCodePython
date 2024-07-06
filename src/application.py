from lc_23_merge_k_sorted_lists.listnode import ListNode
from lc_23_merge_k_sorted_lists.solution import Solution

def main():
    n1 = ListNode(1)
    n1.next = ListNode(4)
    n1.next.next = ListNode(5)
    
    n2 = ListNode(2)
    n2.next = ListNode(3)
    n2.next.next = ListNode(6)
    
    n3 = ListNode(3)
    n3.next = ListNode(4)
    
    lists = [n1, n2, n3]
    res = sol.mergeKLists(lists)
    while res:
        print(res.val)
        res = res.next

if __name__ == '__main__':
    sol = Solution()
    main()
