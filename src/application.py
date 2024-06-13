from lc_2_addtwonumbers.listnode import ListNode
from lc_2_addtwonumbers.solution import Solution

def createList(ls):
    head = None
    tail = head
    
    for i in ls:
        if head is None:
            head = ListNode(i)
            tail = head
        else:
            tail.next = ListNode(i)
            tail = tail.next

    return head

def printList(l):
    while l:
        print(l.val, end=' ')
        l = l.next
    print('\r')

def main():
    l1 = createList([2, 4, 9])
    l2 = createList([0])
    
    ans = sol.addTwoNumbers(l1, l2)
    printList(ans)

if __name__ == '__main__':
    sol = Solution()
    main()
