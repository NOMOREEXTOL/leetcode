class Solution():
    def reverseList(self,head):
        """
        反转链表
        思路：维护两个单链表，原链表每次从头部去除节点，再头插到另外一条链表当中
        28ms,15.1MB(23.18,23.59 % )
        """
        if head is None or head.next is None:
            return head

        newHead = ListNode(head.val)

        pre = head
        cur = head.next
        while cur is not None:
            pre.next = pre.next.next # 取出cur节点,且保证原链表不丢失
            cur.next = newHead
            newHead = cur
            cur = pre.next
        return newHead

    def revserseList2(self,head):
        """
        反转链表思路二：双指针解法
        思路：
        维护头指针和尾指针，每次从头节点取出节点，放入尾指针之后
        32ms,14.9MB(8.25,86.53 % )
        """
        if head is None or head.next is None:
            return head

        cur = head
        while cur.next is not None:
            cur = cur.next
        tail = cur # 尾指针

        cur = head
        while cur != tail:
            head = cur.next
            cur.next = tail.next
            tail.next = cur
            cur = head

        return head










class ListNode():
    def __init__(self,val = 0,next = None):
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
    rawList = ListNode(3)
    reList = s.revserseList2(rawList)
    ListNode.travel(reList)

