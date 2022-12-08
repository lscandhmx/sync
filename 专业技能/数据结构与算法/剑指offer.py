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


# 1.5 链表中环的入口结点

# 题解：官方
# 1.判断链表是否有环。（证明快慢指针一定相遇  https://www.zhihu.com/question/23208893）
# 2.在有环的链表中找到环的入口。
# 那我们现在假定已经是一个有环的链表了，那么这个链表中怎么找到环的入口呢？
# 在慢指针进入链表环之前，快指针已经进入了环，且在里面循环，这才能在慢指针进入环之后，快指针追到了慢指针，不妨假设快指针在环中走了n圈，
# 慢指针在环中走了m圈，它们才相遇，而进入环之前的距离为x，环入口到相遇点的距离为y，
# 相遇点到环入口的距离为z。快指针一共走了x+n(y+z)+y步，
# 慢指针一共走了x+m(y+z)+y，这个时候快指针走的倍数是慢指针的两倍，
# 则x+n(y+z)+y=2(x+m(y+z)+y)，
# 这时候x+y=(n−2m)(y+z)，因为环的大小是y+z，
# 说明从链表头经过环入口到达相遇地方经过的距离等于整数倍环的大小：那我们从头开始遍历到相遇位置，和从相遇位置开始在环中遍历，会使用相同的步数，
# 而双方最后都会经过入口到相遇位置这y个节点，那说明这y个节点它们就是重叠遍历的，那它们从入口位置就相遇了，这我们不就找到了吗？
class Solution:
    def EntryNodeOfLoop(self, pHead):
        #创建个已访问过结点的哈希表
        nodes = set()
        #首先判断链表有无成为环的结点：
        while pHead:                #有结点的情况下：
            if pHead in nodes:      #如果结点存在于哈希表中，就返回结点
                return pHead
            else:
                nodes.add(pHead)     #否则把结点添加到哈希表中
                pHead = pHead.next   #继续遍历下一个结点
        return None                 #无结点就返回None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow = self.hasCycle(pHead)
        if slow == None:
            return None
        # 快指针回到表头
        fast = pHead
        # 再次相遇即是环入口
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow

    # 判断有没有环，返回相遇的地方
    def hasCycle(self, pHead):
        # 先判断链表为空的情况
        if pHead == None:
            return None
        # 快慢双指针
        fast = pHead
        slow = pHead
        # 如果没环快指针会先到链表尾
        while fast and slow:
            # 慢指针移动一步
            slow = slow.next
            # 快指针移动两步
            if fast.next:
                fast = fast.next.next
            else:
                return None
            # 相遇则有环
            if fast == slow:
                return slow
        #到末尾则没有环
        return None


# 1.6 链表中倒数最后k个结点
class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        fast = pHead
        slow = pHead
        #快指针先行k步
        for i in range(0,k):
            if fast != None:
                fast = fast.next
            #达不到k步说明链表过短，没有倒数k
            else:
                return None
        #快慢指针同步，快指针先到底，慢指针指向倒数第k个
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
