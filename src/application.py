from lc_21_merge_two_sorted_lists.listnode import ListNode
from lc_21_merge_two_sorted_lists.solution import Solution

def main():
    n1 = ListNode(1)
    n2 = None # ListNode(1)
    
    res = sol.mergeTwoLists(n1, n2)
    while res:
        print(res.val)
        res = res.next

if __name__ == '__main__':
    sol = Solution()
    main()
