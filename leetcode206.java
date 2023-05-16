/**
 * leetcode206:反转链表
 */

public class leetcode206 {
    public static void main(String[] args) {

    }


    // 思路一：维护两个链表 0ms,40.4MB(100,92.59 %)
    public static ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {return head;}

        ListNode newHead = new ListNode(head.val);

        ListNode cur = head.next;
        ListNode pre = head;

        while (cur != null) {
            pre.next = pre.next.next;
            cur.next = newHead;
            newHead = cur;
            cur = pre.next;
        }
        return newHead;
    }

    // 思路二：原位反转链表 0ms,40.4MB
    public ListNode reverseList2(ListNode head) {
        if (head == null || head.next == null) {return head;}

        ListNode cur = head;
        while (cur.next != null) {
            cur = cur.next;
        }
        ListNode tail = cur; // 尾指针

        cur = head;
        while (cur != tail) {
            head = cur.next;
            cur.next = tail.next;
            tail.next = cur;
            cur = head;
        }
        return head;




    }

}


