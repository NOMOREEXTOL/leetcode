class Solution():
    def swapPairs(self,head):
        """
        两两交换链表中的节点
        16ms,13.1MB(76.48,35.31%)
        """
        FORWARDTIMES = 2

        if head is None or head.next is None:
            return head

        # 不考虑头部节点的情况下，对前两个元素进行反转
        cur = head.next
        head.next = cur.next
        cur.next = head
        head = cur
        cur = cur.next

        # 对前两个元素以后的元素进行反转
        while cur is not None:
            pre = cur
            for i in range(FORWARDTIMES):
                cur = cur.next
                if cur is None:
                    return head
            pre.next.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = cur.next

        return head












class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def travel(head):
        cur = head
        while cur is not None:
            print(cur.val)
            cur = cur.next


if __name__ == '__main__':
    s = Solution()
    rawList = ListNode(1,ListNode(2))
    reList = s.swapPairs(rawList)
    ListNode.travel(reList)


