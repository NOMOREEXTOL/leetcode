class Solution():
    def deleteCircle(self,head):
        """
        记忆化搜索
        1184ms,19.1MB(5.17,64.92%)
        """
        ls = []

        cur = head

        while cur is not None:
            ls.append(cur)
            cur = cur.next
            if cur in ls:
                return cur
        return None


    def deleteCircle2(self,head):
        """
        快慢指针解法
        36ms,19.2MB(67.39,22.93 %)
        """
        slow = fast = head

        while fast is not None:
            fast = fast.next
            if fast is None:return None
            fast = fast.next
            slow = slow.next
            if (fast == slow):break

        if fast is None:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow



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
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(s.deleteCircle2(node1).val)

