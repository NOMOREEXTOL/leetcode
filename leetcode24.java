/**
 * leetcode24:两两交换链表的元素 0ms,39.3MB
 */

public class leetcode24 {
    public static void main(String[] args) {

    }

    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {return head;}

        // 先交换头两个元素，再往后循环
        ListNode cur = head.next;

        head.next = cur.next;
        cur.next = head;
        head = cur;
        cur = cur.next;

        ListNode pre;

        while (cur != null) {
            pre = cur;
            for (int i = 0; i < 2; i++) {
                cur = cur.next;
                if (cur == null) {return head;}
            }

            pre.next.next = cur.next;
            cur.next = pre.next;
            pre.next = cur;
            cur = cur.next;
        }

        return head;

    }

}



