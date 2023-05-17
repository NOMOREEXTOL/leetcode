class Solution():
    def removeNthFromEnd(self,head,n):
        """
        删除链表的倒数第n个节点
        思路：
        先遍历一遍得到总长度，拟删除节点正数下标asIndex = length - n
        再遍历到指定下标删除即可
        16ms,13MB(83.35,70.18%)
        """
        cur = head
        length = 0
        while cur is not None:
            cur = cur.next
            length += 1

        asIndex = length - n
        if asIndex == 0:
            head = head.next
            return head

        cur = head
        pre = None



        # 找到要删除节点
        while asIndex > 0:
            pre = cur
            cur = cur.next
            asIndex -= 1

        pre.next = cur.next

        return head



    def removeVersionOld(self,head,n):
        p = r = head
        if head.next is None:
            return None

        for i in range(n):
            r = r.next
        while r is not None and r.next is not None:
            p = p.next
            r = r.next
        if r is None:
            head = head.next
        else:
            p.next = p.next.next
        return head


    def removeNthFromEnd2(self,head,n):
        """
        题解解法：双指针，采用快慢指针
        快指针先移动n + 1步，然后两指针同步后移，直到快指针为None
        为什么是n + 1步，因为要删除指定节点，那么慢指针必须指向要删除节点的头一个节点
        20ms,13.1MB(58.23,30.92%)
        """
        fast = head
        slow = head

        for i in range(n + 1):
            if fast is None: # 说明提前为None了，那么要删除的就是头结点
                head = head.next
                return head
            fast = fast.next


        while fast is not None:
            fast = fast.next
            slow = slow.next

        # 删除指定节点
        slow.next = slow.next.next

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
    rawList = ListNode(1)
    n = 1
    reList = s.removeNthFromEnd2(rawList,n)
    ListNode.travel(reList)
