from lc_25_reverse_nodes_in_k_group.listnode import ListNode
from lc_25_reverse_nodes_in_k_group.solution import Solution

def main():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    res = sol.reverseKGroup(n1, 6)
    while res:
        print(res.val)
        res = res.next

if __name__ == '__main__':
    sol = Solution()
    main()
