import java.util.ArrayList;

/**
 * leetcode142:环形链表
 * 返回入环的第一个节点索引
 */


public class leetcode142 {
    public static void main(String[] args) {

    }

    // 思路：记录走过的每一个节点，当重复时就是存在环，返回第一个重复的节点，如果没有重复，那么会一直
    // 到null 305ms,42.4MB(2.80,15.44 %)
    public static ListNode deleteCircle(ListNode head) {
        ArrayList<ListNode> records = new ArrayList<>();

        ListNode cur = head;

        while (cur != null) {
            if (records.contains(cur)) {return cur;}
            else {
                records.add(cur);
                cur = cur.next;
            }
        }
        return null; // 说明没找到环，则直接返回null
    }

    // 快慢指针解法：定义一个快指针，每次移动两步，定义一个慢指针，每次移动一步
    // 若二者未相遇，说明没有环，返回null
    // 若二者相遇了，说明有环，此时要找环的入口
    // 找环入口的方法如下：设头结点head到环入口距离为x（为所求），环入口到两指针相遇点的距离为y
    // 两指针相遇点到第二次到达环入口的距离为z，那么则有二者相遇时，
    // 慢指针路程：x + y, 快指针路程：x + y + n(y + z) ,其中n为快指针经历的圈数，在两指针相遇前
    // 快指针可能已经在环里转了好多圈了，再由二者速度差可知 快指针路程 = 慢指针 * 2
    // 则有 2(x + y) = (x + y) + n(y + z) 即 x = n(y + z) - y = (n - 1)(y + z) + z
    // n >= 1,快指针至少转了一圈才能和慢指针相遇，若n == 1,则有x = z,若n不等于1，那么x也是在z 的基础之上
    // 转了若干圈，所以，要求出环的入口，只需要在此时，再定义两个指针，一个从头结点开始，一个从相遇点开始，这两个
    // 指针的相遇点就是环的入口。'

    // 0ms,42.8MB(100,6.13 %)
    public static ListNode deleteCircle2(ListNode head) {
        ListNode fast = head,slow = head;

        // 找相遇点
        while (fast != null) {
            fast = fast.next;
            if (fast == null) {return null;}
            fast = fast.next;
            slow = slow.next;
            if (fast == slow) {break;}
        }

        slow = head;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }
}