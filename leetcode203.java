/**
 * leetcode203:0ms,44.2MB(100,5.93 %)
 */


import java.util.List;

public class leetcode203 {
    public static void main(String[] args) {

    }
    static ListNode removeElements(ListNode head,int val) {
     while ((head != null) && head.val == val) {
         head = head.next;
     }

     if (head == null) {
         return head;
     }

     ListNode cur = head.next;
     ListNode pre = head;

     while (cur != null) {
         if (cur.val == val) {
             cur = cur.next;
             pre.next = cur;
         } else {
             pre = cur;
             cur = cur.next;
         }
     }

     return head;

    }
}




class ListNode {
    int val;
    ListNode next;

    ListNode() {} // 无参构造器
    ListNode(int val) {this.val = val;}
    ListNode(int val,ListNode next) {this.val = val; this.next = next;}

}