class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ReverseList(pHead):
        # write code here
    if (pHead is None):
        return pHead
    if (pHead.next is None):
        return pHead
    p1, p2, p3 = pHead, pHead.next, pHead.next.next
    if (p3 is None):
        p2.next = p1
        p1.next = None
        return p2
    # at least 3 nodes now
    while(p2 is not None):
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    return p1
    # if (pHead is None):
    #     return pHead
    # if (pHead.next is None):
    #     return pHead
    # p1, p2, p3 = pHead, pHead.next, pHead.next.next
    # if (p3 is None):
    #     p2.next = p1
    #     p1.next = None
    #     return p2
    # # at least 3 nodes now
    # p1.next = None
    # while(p3 is not None):
    #     p2.next = p1
    #     p4 = p3.next
    #     p1 = p2
    #     p2 = p3
    #     p3 = p4
    # p2.next = p1
    # return p2

head = ListNode(1)
head2 = head
for i in range(2, 6):
    p = ListNode(i)
    head.next = p
    head = head.next
test = ReverseList(head2)
print(test.val)
