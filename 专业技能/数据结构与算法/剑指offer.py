# 1. 链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



# 1.3 合并两个排序的链表

# 题解：官网
class Solution:
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        head = ListNode(0)
        cur = head
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        if pHead1:
            cur.next = pHead1
        if pHead2:
            cur.next = pHead2
        return head.next


class Solution1:
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
        #一个已经为空了，返回另一个
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        #先用较小的值的节点
        if pHead1.val <= pHead2.val:
            #递归往下
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            #递归往下
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2


# 1.4 两个链表的第一个公共结点
# 题解：官网

class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        return p1


