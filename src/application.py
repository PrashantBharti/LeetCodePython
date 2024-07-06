from lc_24_swap_nodes_in_pairs.listnode import ListNode
from lc_24_swap_nodes_in_pairs.solution import Solution

def main():
    n1 = ListNode(1)

    res = sol.swapPairs(n1)
    while res:
        print(res.val)
        res = res.next

if __name__ == '__main__':
    sol = Solution()
    main()
