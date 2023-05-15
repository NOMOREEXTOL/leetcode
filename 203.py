class Solution():
    def removeElements(self,head,val):
        """
        leetcode203题，给定链表头结点，删除值为val的节点
        49ms,19.7MB(81.34,54.28 %)
        """

        while head is not None and head.val == val:
            head = head.next

        if head is None:
            return head

        cur = head.next
        pre = head

        while cur is not None:
            if cur.val == val:
                cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next

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
    head = ListNode(3,ListNode(1,ListNode(2,ListNode(4,ListNode(2)))))
    head = s.removeElements(head,2)
    ListNode.travel(head)