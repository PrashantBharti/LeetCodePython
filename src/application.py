from lc_19_nth_node_from_end_of_list.listnode import ListNode
from lc_19_nth_node_from_end_of_list.solution import Solution

def main():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    
    n1.next = n2
    n2.next = n3
    n3.next = n4
    
    res = sol.removeNthFromEnd(n1, 1)
    cur = res
    while cur:
        print(cur.val)
        cur = cur.next

if __name__ == '__main__':
    sol = Solution()
    main()
