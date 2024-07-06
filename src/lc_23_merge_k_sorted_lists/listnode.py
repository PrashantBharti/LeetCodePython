class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not self and not other:
            return True
        if not self or not other:
            return False
        return self.val == other.val and self.next == other.next
    
    def __lt__(self, other):
        return self.val < other.val
    
    def __le__(self, other):
        return self.val <= other.val
    
    def __gt__(self, other):
        return self.val > other.val
    
    def __ge__(self, other):
        return self.val >= other.val