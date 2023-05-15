class MyLinkedList():
    """
    324ms,13.7MB(44.44,53.03 %)
    """
    def __init__(self,head = None):
        self.head = head

    def addAtHead(self,val):
        """
        在头结点前插入元素
        """
        node = ListNode(val)

        if self.isEmpty():
            self.head = node
            return

        node.next = self.head
        self.head = node


    def isEmpty(self):
        return not self.head

    def addAtTail(self,val):
        """
        在链表尾部插入元素
        """
        node = ListNode(val)

        if self.isEmpty():
            self.head = node
            return head

        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = node


    def addAtIndex(self,index,val):
        """
        在特定索引位置处插入元素
        """
        node = ListNode(val)
        insertIndex = index

        if self.isEmpty():
            if index == 0:
                self.head = node
                return
            else:
                return

        if index == 0:
            node.next = self.head
            self.head = node
            return

        cur = self.head
        pre = None
        while insertIndex > 0:
            if cur is None:
                if insertIndex == 1:
                    pre.next = node
                    return
                else:
                    return
            else:
                pre = cur
                cur = cur.next
                insertIndex -= 1

        # 退出循环说明一定找到了要插入的位置
        node.next = cur
        pre.next = node


    def deleteAtIndex(self,index):
        """
        删除指定索引处的元素
        """

        if self.isEmpty():
            return

        if index == 0:
            self.head = self.head.next
            return



        cur = self.head
        pre = None
        while index > 0:
            if cur is None:
                return
            else:
                pre = cur
                cur = cur.next
                index -= 1
        if cur is None:
            return
        pre.next = cur.next

    def get(self,index):
        """
        获取指定下标索引位置处的元素
        """
        if self.isEmpty():
            return -1
        cur = self.head

        while index > 0:
            if cur is None:
                return -1
            else:
                cur = cur.next
                index -= 1
        if cur is None:
            return -1
        return cur.val







class ListNode():
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next


if __name__ == '__main__':
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(2)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(3,4)
