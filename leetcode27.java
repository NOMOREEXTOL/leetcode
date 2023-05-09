/**
 *  leetcode27:原位删除数组当中的元素
 *  0ms,40.3MB(100,11.33%)
 */
public class leetcode27 {
    public static void main(String[] args) {

    }

    public static int removeElement(int[] nums,int target) {
        int l = -1;
        int r = l + 1;
        int temp;

        while (r < nums.length) {
            if (nums[r] == target) {
                l++;
                while (r < nums.length && nums[r] == target) {
                    r++;
                }
                if (r == nums.length) {return l;}
                temp = nums[l];
                nums[l] = nums[r];
                nums[r] = temp;
                r = l + 1;
            } else {r++; l++;}
        }
        return l + 1;
    }
}





