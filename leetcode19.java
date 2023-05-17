/**
 * leetcode19: 删除链表的倒数第n个节点
 * 0ms,39.5MB(100,74.93 %)
 */




public class leetcode19 {
    public static void main(String[] args) {

    }

    public static ListNode removeNthFromEnd(ListNode head,int n) {
        int length = 0;
        ListNode cur = head;

        // 遍历计算链表长度
        while (cur != null) {
            cur = cur.next;
            length++;
        }

        int asIndex = length - n;
        if (asIndex == 0) {head = head.next; return head;}

        ListNode pre = head;
        cur = head;
        // 查找要删除节点
        while (asIndex > 0) {
            pre = cur;
            cur = cur.next;
            asIndex--;
        }

        // 删除节点
        pre.next = cur.next;
        return head;
    }


    // 0ms,39.7MB(100,26.32%)
    public static ListNode removeNthFromEnd2(ListNode head,int n) {
        ListNode fast = head;
        ListNode slow = head;

        for (int i = 0; i < n + 1; i++) {
            if (fast == null) {head = head.next; return head;}
            fast = fast.next;
        }

        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }

        slow.next = slow.next.next;
        return head;
    }
}