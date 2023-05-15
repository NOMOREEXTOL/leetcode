/**
 * leetcode707:设计链表
 *  10ms,43.3MB(35.96,5.03 %)
 */

public class leetcode707 {
    public static void main(String[] args) {
        MyLinkedList myLinkedList = new MyLinkedList();
        myLinkedList.addAtHead(1);
        myLinkedList.addAtTail(3);
        myLinkedList.addAtIndex(1, 2);    // 链表变为 1->2->3
        System.out.println(myLinkedList.get(1));              // 返回 2
        myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1->3
        System.out.println(myLinkedList.get(1));              // 返回 3

    }
}


class MyLinkedList {
    private ListNode head;

    MyLinkedList() {}
    MyLinkedList(ListNode head) {this.head = head;}

    public int get(int index) { // 获取指定下标的值
        if (isEmpty()) {return -1;}
        if (index == 0) {return head.val;}

        ListNode cur = head;

        while (index > 0) {
            if (cur == null) {
                return -1;
            } else {
                cur = cur.next;
                index--;
            }
        }
        if (cur == null) {return -1;}
        return cur.val;
    }

    public boolean isEmpty() {
        if (head == null) {return true;}
        else {return false;}
    }

    public void addAtHead(int val) {
        ListNode node = new ListNode(val);
        if (isEmpty()) {this.head = node; return;}

        node.next = head;
        head = node;
    }

    public void addAtIndex(int index,int val) {
        ListNode node = new ListNode(val);
        if (index == 0) {addAtHead(val); return;}
        if (isEmpty()) {return;}

        ListNode cur = head;
        ListNode pre = head;

        while (index > 0) {
            if (cur == null) {
                if (index == 1) {
                    pre.next = node;
                    return;
                } else {return;}
            } else {
                pre = cur;
                cur = cur.next;
                index--;
            }
        }
        node.next = cur;
        pre.next = node;
    }

    public void addAtTail(int val) {
        ListNode node = new ListNode(val);
        if (isEmpty()) {head = node;return;}

        ListNode cur = head;
        while (cur.next != null) {
            cur = cur.next;
        }
        cur.next = node;
    }


    public void deleteAtIndex(int index) {
        if (isEmpty()) {return ;}
        if (index == 0) {head = head.next;return;}

        ListNode cur = head;
        ListNode pre = head;

        while (index > 0) {
            if (cur == null) {return;}
            else {
                pre = cur;
                cur = cur.next;
                index--;
            }
        }

        if (cur == null) {return;}
        pre.next = cur.next;
    }

}






class MyNode {
    public int val;
    public MyNode next;

    MyNode() {}
    MyNode(int val) {this.val = val;}
    MyNode(int val,MyNode next) {this.val = val; this.next = next;}

}